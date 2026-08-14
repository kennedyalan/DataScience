library(tm)
library(dplyr)
library(caret)
library(naivebayes)

setwd("C:/Users/akennedy/Documents/Github/ICC/DataScience/R/Circular/Mineria_de_textos/")
docs <- Corpus(DirSource("Libros", encoding = "UTF-8"))

a_espacio <- content_transformer(function(x, pattern) {
  return (gsub(pattern, " ", x))
})

# Por ahora nada pero mientras vayamos iterando vamos a ir limpiando
palabras_inutiles <- c("dos", "tan", "ser", "aquel", "mas", "pues", "fué", "sino", "cada", "gutenberg", "project", "work", "ebook", "online", "www", "usted", "dijo")

docs_limpio <- tm_map(docs, a_espacio, "-") %>%
  tm_map(a_espacio, ":") %>%
  tm_map(a_espacio, "/") %>%
  tm_map(a_espacio, "'") %>%
  tm_map(a_espacio, "\\|") %>%
  tm_map(a_espacio, "\\.") %>%
  tm_map(a_espacio, ",") %>%
  tm_map(removePunctuation) %>%
  tm_map(content_transformer(tolower)) %>%
  tm_map(removeNumbers) %>%
  tm_map(removeWords, stopwords("spanish")) %>%
  tm_map(removeWords, stopwords("english")) %>%
  tm_map(removeWords, palabras_inutiles) %>%
  tm_map(stripWhitespace)


dtm_crudo <- DocumentTermMatrix(docs)
dtm_limpio <- DocumentTermMatrix(docs_limpio)

dtm_crudo <- removeSparseTerms(dtm_crudo, 0.8)
dtm_limpio <- removeSparseTerms(dtm_limpio, 0.8)

matriz_cruda <- as.matrix(dtm_crudo)
matriz_limpia <- as.matrix(dtm_limpio)

# Esto es para ver si hay mas palabras que eliminar y agregar a la bolsa de palabras inutiles
freq_crudo <- sort(colSums(matriz_cruda), decreasing = TRUE)
head(freq_crudo, 50)

freq_limpio <- sort(colSums(matriz_limpia), decreasing = TRUE)
head(freq_limpio, 50)

# Necesitamos clasificar nosotros los libros, lo hacemos por el titulo
titulos <- rownames(matriz_limpia)

# Seccion b.
categoria <- case_when(
  grepl("cocina|recetas|receta|cocinera|gastronomia|aceite", titulos, ignore.case = TRUE) ~ "cocina",
  grepl("historia|histórico|leyenda|biografía|rebelión|argentina|fundación|tratado|actas|diario", titulos, ignore.case = TRUE) ~ "historia",
  TRUE ~ "otros"
)

categoria <- factor(categoria)
set.seed(123)

idx_train <- createDataPartition(categoria, p = 0.7, list = FALSE)

a_sino <- function(m) {
  df <- as.data.frame(m > 0)
  df[] <- lapply(df, function(col) factor(ifelse(col, "Si", "No"), levels = c("No", "Si")))
  df
}

categoria_train <- categoria[idx_train]
categoria_test  <- categoria[-idx_train]

train_crudo  <- a_sino(matriz_cruda[idx_train, ])
test_crudo   <- a_sino(matriz_cruda[-idx_train, ])
train_limpio <- a_sino(matriz_limpia[idx_train, ])
test_limpio  <- a_sino(matriz_limpia[-idx_train, ])

modelo_crudo  <- naive_bayes(x = train_crudo,  y = categoria_train, laplace = 1)
modelo_limpio <- naive_bayes(x = train_limpio, y = categoria_train, laplace = 1)


prediccion_crudo <- predict(modelo_crudo, test_crudo)
prediccion_limpio <- predict(modelo_limpio, test_limpio)

matriz_conusion_crudo <- confusionMatrix(prediccion_crudo, categoria_test)
matriz_confusion_limpio <- confusionMatrix(prediccion_limpio, categoria_test)

matriz_conusion_crudo$byClass[ , "Sensitivity"]
matriz_confusion_limpio$byClass[ , "Sensitivity"]

print(matriz_confusion_limpio)
print(matriz_conusion_crudo)
