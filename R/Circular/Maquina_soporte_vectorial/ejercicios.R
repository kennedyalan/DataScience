library(e1071)
library(dplyr)

patron1 <- read.csv("Data/patron1.csv")

plot(x = patron1$x, y = patron1$y, col = patron1$clase,
     pch = patron1$clase,
     xlab = "valores x", ylab = "valores y")

patron1$r <- sqrt(patron1$x^2 + patron1$y^2)

boxplot(r ~ clase, data = patron1)

set.seed(123)

training <- patron1 %>% dplyr::sample_frac(0.7)

testing <- dplyr::anti_join(patron1, training, by = "X")

print("Dataset")
print(patron1)

print("Training")
print(training)

print("Testing")
print(testing)

m <- svm(as.factor(clase) ~ r, data = training,
         kernel = "linear",
         scale = FALSE,
         cost = 1)

pred <- predict(m, testing)
mean(pred == testing$clase)
table(pred, testing$clase)


cf <- coef(m)
umbral <- -cf[1]/cf[2]

plot(patron1$r, col = patron1$clase,
     ylab = "r (distancia al centro)", main = "Vista en el mundo r")
abline(h = umbral, col = "red")

plot(patron1$x, patron1$y, col = patron1$clase, pch = patron1$clase,
     xlab = "x", ylab = "y", asp = 1, main = "Vista en el plano (x, y)")
symbols(0, 0, circles = umbral, add = TRUE, inches = FALSE, fg = "red")

