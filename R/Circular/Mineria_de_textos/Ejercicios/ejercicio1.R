library(dplyr)
library(tidytext)
library(tidyr)
library(naivebayes)
library(caret)
library(ggplot2)

tuits_df <- read.csv("tuits.csv", stringsAsFactors = FALSE, fileEncoding = "latin1")

frecuencias <- sort(table(tuits_df$screen_name), decreasing = TRUE)
top3 <- names(frecuencias)[1:3]

cat("Los 3 autores mas frecuentes:\n")
print(frecuencias[1:3])

tuits_df$categoria <- ifelse(tuits_df$screen_name %in% top3,
                             tuits_df$screen_name, "otros")
tuits_df$categoria <- as.factor(tuits_df$categoria)

cat("\nTuits por categoria (las 4 clases):\n")
print(table(tuits_df$categoria))

tuits_df$texto <- gsub("\\<http\\S*\\>|[0-9]", " ", tuits_df$text)
tuits_df$texto <- tolower(tuits_df$texto)

matriz <- tuits_df %>%
  unnest_tokens(input = "texto", output = "palabra") %>%
  count(categoria, status_id, palabra) %>%
  spread(key = palabra, value = n) %>%
  select(-status_id)

matriz[is.na(matriz)] <- 0

palabras <- setdiff(names(matriz), "categoria")
matriz[palabras] <- lapply(matriz[palabras],
                           function(x) factor(ifelse(x > 0, "Si", "No"),
                                              levels = c("No", "Si")))

cat("\nDimension de la matriz (filas x columnas):\n")
print(dim(matriz))

set.seed(2001)
train_idx <- sample(1:nrow(matriz), nrow(matriz) * 0.7)
entrenamiento <- matriz[train_idx, ]
testeo <- matriz[-train_idx, ]

cat("\nTrain:", nrow(entrenamiento), " Test:", nrow(testeo), "\n")

modelo <- naive_bayes(formula = categoria ~ ., data = entrenamiento, laplace = 1)
prediccion <- predict(modelo, testeo)

mc <- confusionMatrix(prediccion, testeo$categoria)

cat("\n=== Matriz de confusion ===\n")
print(mc$table)

cat("\n=== Tasa de aciertos por autor (Sensitivity/Recall) ===\n")
print(round(mc$byClass[, "Sensitivity"], 3))

cat("\nAccuracy global:", round(mc$overall["Accuracy"], 3), "\n")

frec_rel <- as.numeric(table(matriz$categoria)) / nrow(matriz)
df_grafico <- data.frame(
  autor = levels(matriz$categoria),
  frecuencia_relativa = frec_rel,
  tasa_acierto = as.numeric(mc$byClass[, "Sensitivity"])
)

grafico <- ggplot(df_grafico, aes(x = frecuencia_relativa, y = tasa_acierto)) +
  geom_point(size = 4, color = "steelblue") +
  geom_text(aes(label = autor), vjust = -1.2) +
  geom_smooth(method = "lm", se = FALSE, linetype = "dashed", color = "gray50") +
  labs(title = "Tasa de aciertos vs frecuencia relativa por autor",
       x = "Frecuencia relativa", y = "Tasa de aciertos (recall)") +
  expand_limits(y = c(0, 1.1)) +
  theme_minimal()

ggsave("ejercicio1_grafico.png", grafico, width = 8, height = 5, dpi = 100)

cat("\n Ejercicio 2: \n")

categorias <- levels(tuits_df$categoria)

stopwords_es <- tibble(palabra = tm::stopwords("spanish"))

for (cat in categorias) {
  matriz <- tuits_df %>%
    filter(categoria == cat) %>%
    unnest_tokens(input = "texto", output = "palabra") %>%
    count(palabra, sort = TRUE, name = "frecuencia") %>%
    anti_join(stopwords_es, by = "palabra")
  
  png(paste0("nube_", cat, ".png"))
  wordcloud(matriz$palabra, matriz$frecuencia,
            max.words = 500,
            scale = c(4, .2),
            random.order = FALSE)
  dev.off()
}
