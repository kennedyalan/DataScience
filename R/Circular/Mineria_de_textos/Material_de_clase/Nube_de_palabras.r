## Código original

## Parte básica: Nube de palabras

## cargo las librerías
library(tm)
library(wordcloud)

## cargo el corpus de textos a analizar
docs <- Corpus(DirSource("Libros"))

## limpieza del Corpus

# Defino función que manda s un determinado patrón a un espacio en blanco
toSpace <- content_transformer(function(x, pattern) {return (gsub(pattern, " ", x))})

# Aplico la función recién definida definida al corpus
docs <- tm_map(docs, toSpace, "-")
docs <- tm_map(docs, toSpace, ":")
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, toSpace, "’")
docs <- tm_map(docs, toSpace, "‘")
docs <- tm_map(docs, toSpace, "-")
docs <- tm_map(docs,content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)

# Remuevo las palabras sin contenido semántico propio en inglés y en castellano
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removeWords, stopwords("spanish"))

# Elimino los espacios múltiples (Cuando hay varios espacios en blanco juntos queda uno solo)
docs <- tm_map(docs, stripWhitespace)

## Construyo la matriz de palabras x documentos:
dtm <- DocumentTermMatrix(docs)

## Hago la cuenta de frecuencia de las palabras sumando las columnas de la matriz
freq <- colSums(as.matrix(dtm))

## Hago una copia de freq ordenada en forma descendente
ord <- order(freq,decreasing=TRUE)

## Me quedo con las palabras que aparecen más de 500 veces
freq2 <- freq[which(freq>=500)]

## Construyo la nube de palabras
wordcloud(names(freq2),freq2)