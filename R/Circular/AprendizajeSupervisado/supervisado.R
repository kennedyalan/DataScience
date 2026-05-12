library(ggplot2)
library(readr)
library(fastDummies)
library(dbscan)


Mall_Customers <- read_csv("Github/ICC/DataScience/R/Circular/Data/Mall_Customers.csv")


head(Mall_Customers)
# Genre hay que convertirlo a numérico
Mall_Customers <- dummy_cols(Mall_Customers, select_columns = "Genre", remove_selected_columns = TRUE, remove_first_dummy = TRUE)
Mall_Customers
# remove_first_dummy en true hace que elimine la primer columna dummy, en este caso porque la variable categorica genre solo tomaba dos valores
income_spending <- Mall_Customers[, c("Annual Income (k$)", "Spending Score (1-100)")]
income_spending

# Método del codo:
wcss <- numeric(10)
for (i in 1:10) {
  kmeans_model <- kmeans(income_spending, centers = i, nstart = 25, algorithm = "Lloyd")
  wcss[i] <- kmeans_model$tot.withinss
}

# Graficar el metodo del codo:
plot(1:10, wcss, type = "b", main = "Método del Codo",
     xlab = "Numero de clusters", ylab = "WCSS", col = "blue", lwd = 2)

kmeans_model <- kmeans(income_spending, centers = 5, nstart = 25, algorithm = "Lloyd")
y_kmeans <- kmeans_model$cluster

df_clustered <- data.frame(
  Income = income_spending$`Annual Income (k$)`,
  SpendingScore = income_spending$`Spending Score (1-100)`,
  Cluster = as.factor(y_kmeans)
)

ggplot(df_clustered, aes(x = Income, y = SpendingScore, color = Cluster)) +
  geom_point(size = 3) +
  geom_point(data = data.frame(
    Income = kmeans_model$centers[, 1],
    SpendingScore = kmeans_model$centers[, 2]), 
    aes(x = Income, y = SpendingScore),
    color = "black", size = 10, shape = 4, stroke = 2) +
    scale_color_manual(values = c("1" = "red", "2" = "blue", "3" = "green", "4" = "purple", "5" = "orange")) +
    
  
    labs(title = "Clusters de Clientes", 
         x = "Ingreso Anual (k$)", 
         y = "Puntaje de Gastos (1-100)") +
    theme_minimal() + theme(legend.position = "right")

hdb <- hdbscan(income_spending, minPts = 5)
income_spending$cluster <- as.factor(hdb$cluster)

ggplot(income_spending, aes(x = `Annual Income (k$)`, y = `Spending Score (1-100)`, color = cluster)) +
  geom_point(size = 2) +
  labs(title = "Clusters de Clientes con HDBSCAN", 
       x = "Ingreso Anual (k$)", 
       y = "Puntaje de Gastos (1-100)") +
  theme_minimal() + theme(legend.position = "right")

plot(hdb, show_flat = TRUE)
