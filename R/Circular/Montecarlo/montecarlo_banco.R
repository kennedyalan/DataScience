simular_banco <- function(t_max = 14400,
                          p_llegada = 0.02,
                          atencion_min = 1,
                          atencion_max = 150,
                          max_cola = Inf,
                          p_abandono = 0) {
  cola <- numeric(0)
  ocupado_hasta <- 0
  esperas <- numeric(0)
  rechazados <- 0
  abandonos <- 0

  for (t in 1:t_max) {
    if (runif(1) < p_llegada) {
      if (length(cola) >= max_cola) {
        rechazados <- rechazados + 1
      } else {
        cola <- c(cola, t)
      }
    }

    if (p_abandono > 0 && length(cola) > 5) {
      en_riesgo <- (5 + 1):length(cola)
      se_van <- runif(length(en_riesgo)) < p_abandono
      if (any(se_van)) {
        abandonos <- abandonos + sum(se_van)
        cola <- cola[-en_riesgo[se_van]]
      }
    }

    if (t >= ocupado_hasta && length(cola) > 0) {
      esperas <- c(esperas, t - cola[1])
      cola <- cola[-1]
      ocupado_hasta <- t + runif(1, atencion_min, atencion_max)
    }
  }

  list(esperas = esperas, rechazados = rechazados, abandonos = abandonos)
}

resumen <- function(nombre, corridas) {
  esperas <- unlist(lapply(corridas, `[[`, "esperas"))
  promedios <- sapply(corridas, function(c) mean(c$esperas))
  cat("====", nombre, "====\n")
  cat("Clientes atendidos:", length(esperas), "\n")
  cat("Espera promedio:", round(mean(esperas), 1), "seg\n")
  cat("Desvio estandar de las esperas:", round(sd(esperas), 1), "seg\n")
  cat("Desvio estandar del promedio (entre corridas):", round(sd(promedios), 1), "seg\n")
  cat("% que espera mas de 200 seg:", round(100 * mean(esperas > 200), 1), "%\n")
  cat("Rechazados (vieron 5 en cola):", sum(sapply(corridas, `[[`, "rechazados")), "\n")
  cat("Abandonos (se cansaron de esperar):", sum(sapply(corridas, `[[`, "abandonos")), "\n\n")
}

set.seed(42)
n_corridas <- 200

base <- lapply(1:n_corridas, function(i) simular_banco())
ej_11_1 <- lapply(1:n_corridas, function(i) simular_banco(max_cola = 5))
ej_11_2 <- lapply(1:n_corridas, function(i) simular_banco(p_abandono = 0.002))

resumen("Problema base", base)
resumen("Ejercicio 11.1", ej_11_1)
resumen("Ejercicio 11.2", ej_11_2)
