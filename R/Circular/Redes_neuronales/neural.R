library(neuralnet)
data(iris)


iris$setosa <- ifelse(iris$Species == "setosa", 1, 0)

normalize <- function(x){
  return((x - min(x)) / (max(x) - min(x)))
}

iris_norm <- as.data.frame(lapply(iris[,1:4], normalize))
iris_norm$setosa <- iris$setosa

modelo <- neuralnet(
  setosa ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width,
  data = iris_norm,
  hidden = 3,
  linear.output = FALSE
)

plot(modelo)

prediction <- compute(modelo, iris_norm[, 1:4])

head(prediction$net.result)