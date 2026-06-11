library(GA)

set.seed(42)
n_assets <- 5
n_days   <- 252

asset_names    <- c("AAPL", "GOOGL", "MSFT", "AMZN", "TSLA")
annual_returns <- c(0.15,   0.12,   0.18,   0.20,   0.25)
annual_vols    <- c(0.20,   0.18,   0.22,   0.25,   0.40)

daily_returns <- matrix(nrow = n_days, ncol = n_assets)
colnames(daily_returns) <- asset_names

for (i in 1:n_assets) {
  daily_returns[, i] <- rnorm(
    n_days,
    mean = annual_returns[i] / 252,
    sd   = annual_vols[i] / sqrt(252)
  )
}

mu    <- colMeans(daily_returns) * 252
Sigma <- cov(daily_returns) * 252

rf <- 0.02

sharpe_fitness <- function(w) {
  w                <- abs(w) / sum(abs(w))
  portfolio_return <- sum(w * mu)
  portfolio_vol    <- sqrt(t(w) %*% Sigma %*% w)
  (portfolio_return - rf) / portfolio_vol
}

GA_result <- ga(
  type     = "real-valued",
  fitness  = sharpe_fitness,
  lower    = rep(0, n_assets),
  upper    = rep(1, n_assets),
  popSize  = 100,
  maxiter  = 500,
  run      = 50,
  monitor  = FALSE
)

raw_weights     <- GA_result@solution[1, ]
optimal_weights <- raw_weights / sum(raw_weights)
names(optimal_weights) <- asset_names

portfolio_return <- sum(optimal_weights * mu)
portfolio_vol    <- as.numeric(sqrt(t(optimal_weights) %*% Sigma %*% optimal_weights))
sharpe_ratio     <- (portfolio_return - rf) / portfolio_vol

cat("=== Optimal Portfolio ===\n")
for (i in seq_along(asset_names)) {
  cat(sprintf("  %-6s  %.1f%%\n", asset_names[i], optimal_weights[i] * 100))
}
cat(sprintf("\n  Expected Return : %.2f%%\n", portfolio_return * 100))
cat(sprintf("  Volatility      : %.2f%%\n", portfolio_vol * 100))
cat(sprintf("  Sharpe Ratio    : %.4f\n",   sharpe_ratio))

plot(GA_result, main = "Sharpe Portfolio - GA Convergence")

barplot(
  optimal_weights * 100,
  names.arg = asset_names,
  col       = "steelblue",
  ylab      = "Weight (%)",
  main      = "Optimal Portfolio Weights"
)
