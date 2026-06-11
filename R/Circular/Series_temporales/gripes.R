library(readr)
library(lubridate)
library(dplyr)
library(forecast)
library(ggplot2)
library(tseries)

gripes <- read_delim("Gripes.csv", delim = ";")

gripes <- gripes %>%
  mutate(Fecha = make_date(Año, Mes, Dia)) %>%
  arrange(Fecha)

ggplot(gripes, aes(x = Fecha, y = Cantidad)) +
  geom_line(color = "steelblue") +
  geom_smooth(method = "loess", color = "salmon") +
  labs(title = "Número de casos de gripe a lo largo del tiempo",
       x = "Fecha",
       y = "Número de casos de gripe") +
  theme_minimal()

# Transformar a serie temporal
serie_gripes <- ts(
  gripes$Cantidad,
  frequency = 365
)

# Arima
descomposicion <- decompose(serie_gripes)
plot(descomposicion)

resultado_adf <- tseries::adf.test(serie_gripes)
print(resultado_adf)

arima_model <- auto.arima(serie_gripes)
print(arima_model)

predicciones_arima <- forecast(arima_model, h = 3)
print(predicciones_arima)

# Ejercicio 3.1.1
n <- length(serie_gripes)
print(n)

t_index <- 1:n

modelo_lineal <- lm(serie_gripes ~ t_index)
summary(modelo_lineal)

nuevos_t <- data.frame(t_index = c(2804, 2805, 2806))
predicciones_lineales <- predict(modelo_lineal, newdata = nuevos_t)
print(predicciones_lineales)

# Medias móviles

k <- 365
print(n)
cola <- as.numeric(serie_gripes[(n - k + 1):n])

pred1 <- mean(cola)
print(pred1)

cola <- c(cola[-1], pred1)
pred2 <- mean(cola)

cola <- c(cola[-1], pred2)
pred3 <- mean(cola)

print(c(pred1, pred2, pred3))

# Alisado exponencial
modelo_exponencial <- ses(serie_gripes, h = 3)
print(modelo_exponencial$model$par["alpha"])

pred_exponencial <- as.numeric(modelo_exponencial$mean)
print(pred_exponencial)

# Adicionales
modelo_holt <- holt(serie_gripes, h = 3)
print(as.numeric(modelo_holt$mean))

modelo_hw <- hw(serie_gripes, h = 3)
print(as.numeric(modelo_hw$mean))

print(modelo_holt$model$par)

gripes <- gripes %>%
  mutate(DiaSemana = wday(Fecha, label = TRUE, week_start = 7))

gripes %>%
  group_by(DiaSemana) %>%
  summarise(Promedio = mean(Cantidad)) %>%
  print()