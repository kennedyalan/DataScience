library(e1071)

summary(m)
coef(m)

predict(m, data.frame(x = 2.5, y = 2))


set.seed(2)
dfRadial <- data.frame(x = c(rnorm(100, 0,.2), 3*rnorm(100, 0, .5)),
                       y = c(rnorm(100, 0,.2), 3*rnorm(100, 0,.5)),
                       color = rep(c(1,2), each=100))


plot(x = dfRadial$x, y = dfRadial$y, col = dfRadial$color,
     pch = rep(c(15,16), each=100),
     xlab = "valores x1", ylab = "valores x2")

m.lineal <- svm(as.factor(color) ~ x + y, data = dfRadial,
                kernel = "linear", scale = FALSE, cost = 2)

mean(predict(m.lineal) != dfRadial$color)
mean(predict(m) != dfRadial$color)
