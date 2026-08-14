## Clasificaci�n supervisada de textos

# Cargamos las librer�as: Si tienen alg�n error revisen que las tengan instaladas. Eventualmente hay que instalarlas
library(tidyverse)
library(tidytext)
library(naivebayes)
library(tm)
library(caret)

# Nos paramos en el directorio de trabajo (Cada uno elegir� un directorio donde tenga permisos para leer y escribir
setwd("d:/Dropbox/Curso Elearning Diplo en BI/MLP/Materiales/Miner�a de Texto")

# Web scrapping v 1.0: Nos descargamos de la web un archivo con distintos tweets
download.file(url = "https://raw.githubusercontent.com/jboscomendoza/rpubs/master/bayes_twitter/tuits_bayes.csv", destfile = "tuits.csv")

# Convertimos el archivo con tweets a un tibble porque as� lo demandan las funciones que usaremos despu�s
tuits_df <- read.csv("tuits.csv", stringsAsFactors = F, fileEncoding = "latin1") %>% tbl_df

# Generamos una funci�n para remover partes del texto que no me interesan por falta de valor sem�ntico
quitar_url <- function(texto) {
  gsub("\\<http\\S*\\>|[0-9]", " ", texto)
}

# Mostramos como queda el tibble 
tuits_df %>%
  unnest_tokens(input = "text", output = "palabra") %>%
  count(screen_name, status_id, palabra) %>%
  spread(key = palabra, value = n)

# Creamos una funci�n para crear la matriz de palabras por documento
crear_matriz <- function(tabla) {
  tabla %>%
    mutate(text = quitar_url(text)) %>%
    unnest_tokens(input = "text", output = "palabra") %>%
    count(screen_name, status_id, palabra) %>%
    spread(key = palabra, value = n) %>%
    select(-status_id)
}

# Generamos la matriz usando la funci�n que acabamos de generar
ejemplo_matriz <-
  tuits_df %>%
  mutate(screen_name = ifelse(screen_name == "MSFTMexico", screen_name, "Otro"),
         screen_name = as.factor(screen_name)) %>%
  crear_matriz

# Agrupamos los usuarios que no nos interesan bajo la categor�a "Otro"
elegir_usuario <- function(nombres, usuario) {as.factor(ifelse(nombres %in% usuario, nombres, "Otro"))}

# Separamos en train y test
set.seed(2001)
ejemplo_entrenamiento <- sample_frac(ejemplo_matriz, .7)
ejemplo_prueba <- setdiff(ejemplo_matriz, ejemplo_entrenamiento)

# Generamos una funci�n para crear las listas que vamos utilizar
crear_sets <- function(tabla, prop = .7) {
  lista_sets <- list()
  lista_sets$train <- sample_frac(tabla, prop)
  lista_sets$test  <- setdiff(tabla, lista_sets[["train"]])
  lista_sets
}

# Creamos el modelo: Tener en cuenta que podr�amos usar muchos (SVM, NB, etc.)
ejemplo_modelo <- naive_bayes(formula = screen_name ~ .,  data = ejemplo_entrenamiento)
ejemplo_prediccion <- predict(ejemplo_modelo, ejemplo_prueba)

# Miramos que nos di�
head(ejemplo_prediccion, 25)

# Consultamos la matriz de confusi�n
confusionMatrix(ejemplo_prediccion, ejemplo_prueba[["screen_name"]])

