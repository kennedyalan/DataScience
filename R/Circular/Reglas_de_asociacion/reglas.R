library(arules)
library(arulesViz)

data("Groceries")

summary(Groceries)

reglas <- apriori(
  Groceries,
  parameter = list(
    support = 0.001,
    confidence = 0.3,
    minlen = 2
  )
)

reglas_lift <- sort(reglas, by = "lift")

inspect(head(reglas_lift, 10))

plot(
  reglas_lift[1:20],
  method = "graph",
  interactive = TRUE,
  engine = "htmlwidget"
)