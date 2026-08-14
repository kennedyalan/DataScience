library(tm)
library(wordcloud)

docs <- Corpus(DirSource("Libros", encoding = "UTF-8"))

aEspacio <- content_transformer(function(x, pattern) gsub(pattern, " ", x))

docs <- tm_map(docs, aEspacio, "-")

docs <- tm_map(docs, aEspacio, ":")

docs <- tm_map(docs, removePunctuation)

docs <- tm_map(docs, content_transformer(tolower))

docs <- tm_map(docs, removeNumbers)

docs <- tm_map(docs, removeWords, stopwords("spanish"))

docs <- tm_map(docs, removeWords, stopwords("english"))

# Una palabra es lo que está entre espacios en blanco. Al reemplazar todo
# lo que reemplazamos, el algoritmo va a detectar palabras que son basicamente " "
docs <- tm_map(docs, stripWhitespace)

dtm <- DocumentTermMatrix(docs)
freq <- colSums(as.matrix(dtm))
freq <- sort(freq, decreasing = TRUE)

cat("Dimension de la matriz (documentos x palabras):\n")
print(dim(dtm))
cat("\nTop 15 palabras mas frecuentes:\n")
print(head(freq, 15))

png("clase_nube.png", width = 800, height = 600)
wordcloud(names(freq), freq, max.words = 100, scale = c(4, 0.5),
          random.order = FALSE, colors = brewer.pal(8, "Dark2"))
dev.off()
cat("\nNube guardada en clase_nube.png\n")
