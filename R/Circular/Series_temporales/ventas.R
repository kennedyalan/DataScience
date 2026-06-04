library(readxl)
library(ggplot2)
library(dplyr)
library(lubridate)
library(scales)
library(tseries)
library(forecast)

df <- read_xlsx("../Data/datos_ventas.xlsx")
df$Fecha <- as.Date(df$Fecha)
df$DiaSemana <- wday(df$Fecha, label = TRUE, abbr = FALSE, week_start = 1)
df$NumeroDia <- wday(df$Fecha, week_start = 1)
df$EsFinDeSemana <- ifelse(df$NumeroDia >= 6, "Fin de semana", "Día laboral")
df$Promocion <- factor(df$Promocion, levels = c(0, 1), labels = c("Sin promoción", "Con promoción"))
df$Feriado <- factor(df$Feriado, levels = c(0, 1), labels = c("No feriado", "Feriado"))


# ============================================================
# 1. EXPLORACIÓN INICIAL
# ============================================================

ggplot(df, aes(x = Fecha, y = Ventas)) +
  geom_line(color = "#2C7BB6", linewidth = 0.8) +
  geom_point(aes(color = Promocion, shape = Feriado), size = 3) +
  geom_smooth(method = "loess", se = TRUE, color = "#D7191C", linetype = "dashed", alpha = 0.2) +
  scale_color_manual(values = c("Sin promoción" = "#2C7BB6", "Con promoción" = "#F46D43")) +
  scale_x_date(date_breaks = "5 days", date_labels = "%d %b") +
  labs(
    title = "Serie Temporal de Ventas Diarias — Enero 2025",
    subtitle = "Puntos naranjas = días con promoción | Triángulos = feriados | Línea roja = tendencia suavizada",
    x = "Fecha",
    y = "Cafés vendidos",
    color = "Promoción",
    shape = "Feriado"
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "bottom")


# ============================================================
# 2. ANÁLISIS DE PATRONES
# ============================================================

ggplot(df, aes(x = Fecha, y = Ventas, fill = EsFinDeSemana)) +
  geom_col(alpha = 0.85) +
  scale_fill_manual(values = c("Día laboral" = "#74ADD1", "Fin de semana" = "#F46D43")) +
  scale_x_date(date_breaks = "3 days", date_labels = "%d") +
  labs(
    title = "Ventas por Día — Diferenciando semana vs fin de semana",
    subtitle = "Se observa estacionalidad semanal: los fines de semana concentran más ventas",
    x = "Día de enero",
    y = "Cafés vendidos",
    fill = NULL
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "bottom")

ventas_por_dia <- df %>%
  group_by(DiaSemana, NumeroDia) %>%
  summarise(
    VentasMedia = mean(Ventas),
    VentasSD = sd(Ventas),
    .groups = "drop"
  ) %>%
  arrange(NumeroDia)

ggplot(ventas_por_dia, aes(x = DiaSemana, y = VentasMedia, fill = VentasMedia)) +
  geom_col(show.legend = FALSE) +
  geom_errorbar(aes(ymin = VentasMedia - VentasSD, ymax = VentasMedia + VentasSD),
                width = 0.3, color = "gray30") +
  geom_text(aes(label = round(VentasMedia, 0)), vjust = -0.5, size = 4) +
  scale_fill_gradient(low = "#ABD9E9", high = "#D7191C") +
  labs(
    title = "Ventas Promedio por Día de la Semana",
    subtitle = "Barras de error muestran la desviación estándar entre semanas",
    x = "Día de la semana",
    y = "Ventas promedio"
  ) +
  theme_minimal(base_size = 13)

media_movil <- df %>%
  mutate(MM3 = zoo::rollmean(Ventas, k = 3, fill = NA, align = "center"),
         MM7 = zoo::rollmean(Ventas, k = 7, fill = NA, align = "center"))

ggplot(media_movil, aes(x = Fecha)) +
  geom_line(aes(y = Ventas), color = "gray60", alpha = 0.7, linewidth = 0.7) +
  geom_line(aes(y = MM3), color = "#4DAC26", linewidth = 1, linetype = "dashed") +
  geom_line(aes(y = MM7), color = "#D01C8B", linewidth = 1.2) +
  scale_x_date(date_breaks = "5 days", date_labels = "%d %b") +
  labs(
    title = "Ventas con Medias Móviles",
    subtitle = "Gris = ventas reales | Verde = MM(3 días) | Rosa = MM(7 días)",
    x = "Fecha",
    y = "Cafés vendidos"
  ) +
  theme_minimal(base_size = 13)


# ============================================================
# 3. INFLUENCIA DE VARIABLES EXTERNAS
# ============================================================

ggplot(df, aes(x = Promocion, y = Ventas, fill = Promocion)) +
  geom_boxplot(alpha = 0.7, show.legend = FALSE) +
  geom_jitter(aes(color = Promocion), width = 0.15, size = 2.5, show.legend = FALSE) +
  scale_fill_manual(values = c("Sin promoción" = "#74ADD1", "Con promoción" = "#F46D43")) +
  scale_color_manual(values = c("Sin promoción" = "#2C7BB6", "Con promoción" = "#D73027")) +
  stat_summary(fun = mean, geom = "point", shape = 18, size = 5, color = "black") +
  labs(
    title = "Efecto de las Promociones en las Ventas",
    subtitle = "Diamante negro = promedio | Puntos = días individuales",
    x = NULL,
    y = "Cafés vendidos"
  ) +
  theme_minimal(base_size = 13)

cat("=== EFECTO PROMOCIÓN ===\n")
df %>%
  group_by(Promocion) %>%
  summarise(
    N = n(),
    Media = mean(Ventas),
    Mediana = median(Ventas),
    SD = sd(Ventas)
  ) %>%
  print()

ggplot(df, aes(x = Temperatura, y = Ventas)) +
  geom_point(aes(color = EsFinDeSemana, size = ifelse(Promocion == "Con promoción", 4, 2)),
             alpha = 0.8, show.legend = TRUE) +
  geom_smooth(method = "lm", se = TRUE, color = "#D7191C", alpha = 0.2) +
  scale_color_manual(values = c("Día laboral" = "#74ADD1", "Fin de semana" = "#F46D43")) +
  labs(
    title = "Relación entre Temperatura y Ventas",
    subtitle = "Puntos más grandes = días con promoción | Línea roja = tendencia lineal",
    x = "Temperatura (°C)",
    y = "Cafés vendidos",
    color = "Tipo de día"
  ) +
  guides(size = "none") +
  theme_minimal(base_size = 13)

cat("\n=== CORRELACIÓN TEMPERATURA vs VENTAS ===\n")
cat("Correlación de Pearson:", round(cor(df$Ventas, df$Temperatura), 3), "\n")
cat("Nota: sin controlar por día de semana\n")

ggplot(df, aes(x = Feriado, y = Ventas, fill = Feriado)) +
  geom_boxplot(alpha = 0.7, show.legend = FALSE) +
  geom_jitter(aes(color = Feriado), width = 0.1, size = 3, show.legend = FALSE) +
  scale_fill_manual(values = c("No feriado" = "#74ADD1", "Feriado" = "#FDAE61")) +
  scale_color_manual(values = c("No feriado" = "#2C7BB6", "Feriado" = "#D73027")) +
  labs(
    title = "Ventas en Feriados vs Días Normales",
    subtitle = "Solo hay 1 feriado (1 de enero) en el dataset",
    x = NULL,
    y = "Cafés vendidos"
  ) +
  theme_minimal(base_size = 13)


# ============================================================
# 4. DETECCIÓN DE ANOMALÍAS
# ============================================================

stats <- df %>%
  group_by(DiaSemana) %>%
  mutate(
    MediaDia = mean(Ventas),
    SDDia = sd(Ventas),
    ZScore = (Ventas - MediaDia) / SDDia
  ) %>%
  ungroup()

umbral_zscore <- 1.5
anomalias <- stats %>%
  filter(abs(ZScore) > umbral_zscore) %>%
  arrange(desc(abs(ZScore)))

cat("\n=== DÍAS ANÓMALOS (Z-Score > 1.5 dentro de su día de semana) ===\n")
anomalias %>%
  select(Fecha, DiaSemana, Ventas, Temperatura, Promocion, Feriado, ZScore) %>%
  print()

ggplot(stats, aes(x = Fecha, y = Ventas)) +
  geom_line(color = "#74ADD1", linewidth = 0.8) +
  geom_point(data = filter(stats, abs(ZScore) <= umbral_zscore),
             color = "#2C7BB6", size = 2.5) +
  geom_point(data = filter(stats, abs(ZScore) > umbral_zscore),
             aes(color = "Anomalía"), size = 4, shape = 8, stroke = 1.5) +
  geom_text(data = filter(stats, abs(ZScore) > umbral_zscore),
            aes(label = format(Fecha, "%d/%m")),
            vjust = -1, hjust = 0.5, size = 3.5, color = "#D73027") +
  scale_color_manual(values = c("Anomalía" = "#D73027")) +
  scale_x_date(date_breaks = "5 days", date_labels = "%d %b") +
  labs(
    title = "Detección de Anomalías en la Serie de Ventas",
    subtitle = "Asteriscos rojos = días con Z-Score > 1.5 respecto al promedio de su día de semana",
    x = "Fecha",
    y = "Cafés vendidos",
    color = NULL
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "bottom")

ggplot(stats, aes(x = Fecha, y = ZScore)) +
  geom_hline(yintercept = c(-umbral_zscore, umbral_zscore),
             linetype = "dashed", color = "#D73027", alpha = 0.7) +
  geom_hline(yintercept = 0, linetype = "solid", color = "gray50") +
  geom_col(aes(fill = ifelse(abs(ZScore) > umbral_zscore, "Anómalo", "Normal")), alpha = 0.8) +
  scale_fill_manual(values = c("Normal" = "#74ADD1", "Anómalo" = "#D73027")) +
  scale_x_date(date_breaks = "5 days", date_labels = "%d %b") +
  labs(
    title = "Z-Score de Ventas por Día (relativo al promedio del día de semana)",
    subtitle = "Líneas punteadas = umbral ±1.5 | Rojo = días atípicos",
    x = "Fecha",
    y = "Z-Score",
    fill = NULL
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "bottom")


# ============================================================
# 5. PANEL RESUMEN FINAL
# ============================================================

cat("\n\n================================================================\n")
cat("REFLEXIÓN FINAL\n")
cat("================================================================\n\n")

cat("1. FACTORES QUE MEJOR EXPLICAN LA VARIACIÓN DE VENTAS:\n")
cat("   - Día de la semana: es el factor más determinante. Los sábados\n")
cat("     y domingos duplican o triplican las ventas de los lunes/martes.\n")
cat("     Esto genera una estacionalidad semanal muy marcada.\n")
cat("   - Promociones: elevan las ventas notablemente en cualquier día.\n")
cat("     El 19-ene (domingo + promoción) alcanzó el máximo del período.\n\n")

cat("2. VARIABLES QUE AGREGARÍA PARA MEJORAR LA PREDICCIÓN:\n")
cat("   - Día de la semana (si no estuviera ya implícito en la fecha)\n")
cat("   - Eventos especiales o locales (partidos, conciertos cerca)\n")
cat("   - Lluvia o clima adverso (¿la gente va menos cuando llueve?)\n")
cat("   - Semana del mes (¿cambia el comportamiento post-cobro?)\n")
cat("   - Competidores cercanos con ofertas simultáneas\n\n")

cat("3. DIFICULTADES PARA PREDECIR ESTA SERIE:\n")
cat("   - Solo 30 días de datos: no hay suficiente historia para detectar\n")
cat("     patrones mensuales o anuales con certeza.\n")
cat("   - Los días de feriado tienen comportamiento especial (el 1-ene\n")
cat("     fue miércoles con ventas de fin de semana = 190), pero con\n")
cat("     un solo feriado no se puede generalizar.\n")
cat("   - Las promociones tienen efecto comprobable pero solo hay 4\n")
cat("     observaciones con promoción, lo que limita la estimación.\n")
cat("   - La temperatura covaría con el día de semana (si los fines de\n")
cat("     semana sistemáticamente tienen más/menos temperatura), lo que\n")
cat("     hace difícil separar su efecto real.\n")


serie_ventas <- ts(
  df$Ventas,
  frequency = 7
)

plot(serie_ventas,
     main = "Serie temporal de ventas",
     ylab = "Cafés vendidos",
     xlab = "Días"
)

descomposicion <- decompose(serie_ventas)

plot(descomposicion)

resultado_adf <- tseries::adf.test(serie_ventas)
print(resultado_adf)

modelo_arima <- auto.arima(serie_ventas)
summary(modelo_arima)

plot(
  fitted(modelo_arima),
  type = "l",
  col = "red",
  main = "Valores Ajustados ARIMA",
  ylab = "Ventas Ajustadas",
  xlab = "Tiempo"
)

plot(
  serie_ventas,
  type = "l",
  col = "blue",
  main = "Serie Real vs Ajustada",
  ylab = "Ventas",
  xlab = "Tiempo"
)

lines(
  fitted(modelo_arima),
  col = "red",
  lwd = 2
)

legend(
  "topright",
  legend = c("Real", "Ajustado"),
  col = c("blue", "red"),
  lty = 1
)