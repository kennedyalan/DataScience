###############################################################
# REDES BAYESIANAS EN R
###############################################################

# install.packages("bnlearn")
# install.packages("igraph")

library(bnlearn)
library(igraph)

###############################################################
# 1. GENERAR DATOS
###############################################################

set.seed(123)

n <- 1000

edad <- sample(
  c("Joven","Adulto","Mayor"),
  n,
  replace = TRUE,
  prob = c(0.35,0.45,0.20)
)

ingreso <- sample(
  c("Bajo","Medio","Alto"),
  n,
  replace = TRUE,
  prob = c(0.30,0.50,0.20)
)

###############################################################
# compras dependen de edad e ingreso
###############################################################

compras <- character(n)

for(i in 1:n){
  
  if(ingreso[i]=="Alto" & edad[i]=="Adulto"){
    
    compras[i] <- sample(
      c("Bajas","Medias","Altas"),
      1,
      prob=c(0.05,0.25,0.70)
    )
    
  }else if(ingreso[i]=="Alto"){
    
    compras[i] <- sample(
      c("Bajas","Medias","Altas"),
      1,
      prob=c(0.10,0.35,0.55)
    )
    
  }else if(ingreso[i]=="Medio" & edad[i]=="Adulto"){
    
    compras[i] <- sample(
      c("Bajas","Medias","Altas"),
      1,
      prob=c(0.20,0.55,0.25)
    )
    
  }else if(ingreso[i]=="Medio"){
    
    compras[i] <- sample(
      c("Bajas","Medias","Altas"),
      1,
      prob=c(0.35,0.50,0.15)
    )
    
  }else{
    
    compras[i] <- sample(
      c("Bajas","Medias","Altas"),
      1,
      prob=c(0.75,0.20,0.05)
    )
    
  }
  
}

###############################################################
# Respuesta a campaña
###############################################################

responde <- character(n)

for(i in 1:n){
  
  if(compras[i]=="Altas" & ingreso[i]=="Alto"){
    
    responde[i] <- sample(
      c("Si","No"),
      1,
      prob=c(0.90,0.10)
    )
    
  }else if(compras[i]=="Altas"){
    
    responde[i] <- sample(
      c("Si","No"),
      1,
      prob=c(0.75,0.25)
    )
    
  }else if(compras[i]=="Medias"){
    
    responde[i] <- sample(
      c("Si","No"),
      1,
      prob=c(0.50,0.50)
    )
    
  }else{
    
    responde[i] <- sample(
      c("Si","No"),
      1,
      prob=c(0.15,0.85)
    )
    
  }
  
}

###############################################################
# DATASET (IMPORTANTE: FACTORES)
###############################################################

datos <- data.frame(
  
  edad = factor(edad),
  
  ingreso = factor(ingreso),
  
  compras = factor(compras),
  
  responde = factor(responde)
  
)

###############################################################
# Verificar
###############################################################

str(datos)

head(datos)

summary(datos)

###############################################################
# RED BAYESIANA
###############################################################

red <- model2network(
  "[edad][ingreso][compras|edad:ingreso][responde|compras:ingreso]"
)

###############################################################
# Dibujar con igraph
###############################################################

aristas <- matrix(c(
  
  "edad","compras",
  
  "ingreso","compras",
  
  "ingreso","responde",
  
  "compras","responde"
  
), byrow=TRUE, ncol=2)

g <- graph_from_edgelist(aristas, directed=TRUE)

plot(
  g,
  layout=layout_as_tree(g),
  vertex.size=35,
  vertex.label.cex=1,
  edge.arrow.size=0.5
)

###############################################################
# AJUSTAR LA RED
###############################################################

modelo <- bn.fit(red, datos)

###############################################################
# Ver tablas de probabilidad
###############################################################

modelo

modelo$compras

modelo$responde

###############################################################
# PREDICCIÓN
###############################################################

clientes <- data.frame(
  
  edad=factor(
    c("Adulto","Joven","Mayor","Adulto"),
    levels=levels(datos$edad)
  ),
  
  ingreso=factor(
    c("Alto","Bajo","Medio","Alto"),
    levels=levels(datos$ingreso)
  ),
  
  compras=factor(
    c("Altas","Bajas","Medias","Medias"),
    levels=levels(datos$compras)
  )
  
)

clientes$responde <- predict(
  modelo,
  node="responde",
  data=clientes
)

###############################################################
# APRENDER LA ESTRUCTURA
###############################################################

estructura <- hc(datos)

print(estructura)

###############################################################
# Dibujar estructura aprendida
###############################################################

g2 <- graph_from_data_frame(
  arcs(estructura),
  directed=TRUE
)

plot(
  g2,
  layout=layout_as_tree(g2),
  vertex.size=35,
  vertex.label.cex=1,
  edge.arrow.size=0.5
)

###############################################################
# Ajustar estructura aprendida
###############################################################

modelo2 <- bn.fit(
  estructura,
  datos
)

modelo2

###############################################################
# Distribuciones
###############################################################

table(datos$edad)

table(datos$ingreso)

table(datos$compras)

table(datos$responde)

###############################################################
# Tabla cruzada
###############################################################

xtabs(
  ~ingreso+compras+responde,
  datos
)
