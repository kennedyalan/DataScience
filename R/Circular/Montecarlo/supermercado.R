## Preparación de datos
lleg <- read.csv("llegadaClientes.csv")

head(lleg)

lleg$X<-NULL

d <- nrow(lleg)
llegp <- numeric(d)
for(i in 1:d) {llegp[i] <- sum(lleg[i,])/ncol(lleg)}
plot(llegp)

suavizar <- function(x,n) 
{
  n <- max(1,floor(n))
  m <- length(x)
  y <- x
  
  for(j in 1:n)
  {
    y <- suavizar2(y)
  }
  
  return(y)
}


suavizar2 <- function(x) 
{
  m <- length(x)
  y <- numeric(m)
  
  y[1] <- (x[1]+x[2])/2
  y[m] <- (x[m-1]+x[m])/2
  for(i in 2:(m-1))
  {
    y[i] <- (x[i-1]+2*x[i]+x[i+1])/4
  }
  return(y)
}

llegs <- suavizar(llegp,1000)
llegs <- as.data.frame(llegs)
colnames(llegs) <- "dclientes"
write.csv(llegs,"dclientes.txt")

## duraciones de atención

dur <- read.csv("Duraciones.csv")
dur$X <- NULL

hist(dur$dur)

duracionMedia <- sum(dur$dur)/nrow(dur)

duracionMedia

sdDuracion <- sd(dur$dur)

sdDuracion^2

plot(density(dur$dur))
lines(dpois(0:260,200),col=2)


## Simulador de montecarlo


## vector para guardar los resultados del histograma de duraciones de atención

duracionesatencion <- numeric(d)
duracionesatencion[] <- 0

## cantidad de colas disponibles

ncolas <- 50

colas <- numeric(ncolas)
inicioatencion <- numeric(ncolas)
inicioatencion[] <- 0

## dataframe con las longitudes de las colas

longitudes <- matrix(nrow = d, ncol = ncolas, 0)
longitudes <- as.data.frame(longitudes)


## probabilidades de llegada de clientes como función del tiempo

dclientes <- read.csv("dclientes.txt")

## distribución de probabilidades de duración de la atención acumuladas

## construyo la distribución de probabilidad acumulada para la atenciones

dmax <- max(dur$dur)

datencion <- numeric(dmax)
datencion[] <- 0
for(i in 1:dmax)
{
  datencion[i] <- length(which(dur$dur<i))/nrow(dur)
}

write.csv(datencion,"datencion.csv")


llegaron <- 0

for(i in 1:d)
{
  
  llegan <- rpois(1,dclientes$dcliente[i])
  
  ## asigno a colas a los clientes que llegan
  
  if(llegan>0)
  {
    for(j in 1:llegan)
    {
      ## cada prospecto va a parar a la cola más corta
      colamin <- min(which(colas == min(colas)))
      colas[colamin] <- colas[colamin]+1
      llegaron <- llegaron + 1
    }
  }
  
  ## ajusto los inicios de atención
  
  for(j in 1:ncolas)
  {
    if(colas[j]>0 & inicioatencion[j]==0)
    {
      inicioatencion[j] <- i
    }		
  }
  
  for(k in 1:ncolas)
  {
    ## para cada cola me fijo si tiene a alguien 
    
    if(colas[k]>0)
    {
      ## calculo el tiempo de atención transcurrido
      dt <- i-inicioatencion[k]
      
      ## calculo la probabilidad de haber completado la atención
      if(dt>0)
      {
        p <- datencion[dt+1]
      }
      else
      {
        p<-0
      }
      
      ## decido si se completó la atención
      if(p>runif(1))
      {
        colas[k] <- colas[k]-1
        duracionatencion <- i - inicioatencion[k]
        inicioatencion[k] <- 0
        duracionesatencion[duracionatencion] <- duracionesatencion[duracionatencion] + 1
        
      }
    }
  }
  ## guardo la longitud de las colas en este instante
  longitudes[i,] <- colas
}

longitudPromedio <- numeric(d)

for(m in 1:d){longitudPromedio[m]<-sum(longitudes[m,])}

plot(duracionesatencion[1:max(which(duracionesatencion>0))], main = "Distribución de duraciones de atención", xlab = "Duración de atención", ylab = "Frecuencia")

plot(longitudPromedio/ncolas, main = "Evolucion de la longitud promedio de las colas", xlab = "Tiempo", ylab = "Longitud promedio de las colas")

length(which(longitudes[,1]>1))/50400
