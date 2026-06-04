library(neuralnet)
library(MASS)

data(Boston)

summary(Boston)

normalize <- function(x){
  return((x - min(x)) / (max(x) - min(x)))
}

boston_norm <- as.data.frame(lapply(Boston, normalize))

set.seed(123)

index <- sample(1:nrow(boston_norm), round(0.7 * nrow(boston_norm)))

train <- boston_norm[index, ]
test <- boston_norm[-index, ]

modelo_reg <- neuralnet(
  medv ~ crim + zn + indus + nox + rm + age + dis + tax + ptratio + lstat,
  data = train,
  hidden = 5,
  linear.output = TRUE
)

plot(modelo_reg)

pred <- compute(modelo_reg, test[, c(
  "crim", "zn", "indus", "nox", "rm",
  "age", "dis", "tax", "ptratio", "lstat"
)])

head(pred$net.result)

min_medv <- min(Boston$medv)
max_medv <- max(Boston$medv)

valor_real <- pred$net.result * (max_medv - min_medv) + min_medv
valor_real