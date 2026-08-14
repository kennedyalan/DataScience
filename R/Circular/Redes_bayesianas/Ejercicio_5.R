library(bnlearn)

red <- model2network(
  "[A][S][T|A][B|S][L|S][E|T:L][R|E][D|E:B]"
)

dim_names <- c("si", "no")

cpt_A <- array(
  c(0.01, 0.99),
  dim = 2,
  dimnames = list(A = dim_names)
)

cpt_S <- array(
  c(0.5, 0.5),
  dim = 2,
  dimnames = list(S = dim_names)
)

cpt_T <- array(
  c(0.05, 0.95, 0.01, 0.99),
  dim = c(2, 2),
  dimnames = list(T = dim_names, A = dim_names)
)

cpt_B <- array(
  c(0.6, 0.4, 0.3, 0.7),
  dim = c(2, 2),
  dimnames = list(B = dim_names, S = dim_names)
)

cpt_L <- array(
  c(0.1, 0.9, 0.01, 0.99),
  dim = c(2, 2),
  dimnames = list(L = dim_names, S = dim_names)
)

cpt_E <- array(
  c(1, 0, 1, 0, 1, 0, 0, 1),
  dim = c(2, 2, 2),
  dimnames = list(E = dim_names, T = dim_names, L = dim_names)
)

cpt_R <- array(
  c(0.98, 0.02, 0.05, 0.95),
  dim = c(2, 2),
  dimnames = list(R = dim_names, E = dim_names)
)

cpt_D <- array(
  c(0.90, 0.10, 0.80, 0.20, 0.70, 0.30, 0.10, 0.90),
  dim = c(2, 2, 2),
  dimnames = list(D = dim_names, E = dim_names, B = dim_names)
)

modelo <- custom.fit(
  red,
  dist = list(
    A = cpt_A, S = cpt_S, T = cpt_T, B = cpt_B,
    L = cpt_L, E = cpt_E, R = cpt_R, D = cpt_D
  )
)

print(modelo)

set.seed(123)
cpquery(
  modelo, 
  event = (L == "si"),
  evidence = (R == "si" & S == "no" & A == "si"),
  n = 10^6
)

cpquery(
  modelo, 
  event = (L == "si"),
  evidence = (R == "si" & S == "si" & A == "si"),
  n = 10^6
)