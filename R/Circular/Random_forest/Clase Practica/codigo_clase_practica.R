h<-read.csv("NoCategoricos5.csv",sep=";")
x <- runif(nrow(h))

## Probamos Bootstrap

h1 <- h[which(x<1/3.),]
h2 <- h[which(x>=1/3. & x<2/3.),]
h3 <- h[which(x>=2/3.) ,]

hTrainAB <- rbind(h1,h2)
hTestAB <- h3

hTrainAC <- rbind(h1,h3)
hTestAC <- h2

hTrainBC <- rbind(h2,h3)
hTestBC <- h1

library(rpart)

tAB <- rpart(data = hTrainAB, formula = R ~ A + B + C + D + E)
tBC <- rpart(data = hTrainBC, formula = R ~ A + B + C + D + E)
tAC <- rpart(data = hTrainAC, formula = R ~ A + B + C + D + E)

pAB <- predict(tAB, newdata = hTestAB)
pBC <- predict(tBC, newdata = hTestBC)
pAC <- predict(tAC, newdata = hTestAC)

errAB <- sum((as.vector(pAB)-hTestAB$R)^2)/nrow(hTestAB)
errBC <- sum((as.vector(pBC)-hTestBC$R)^2)/nrow(hTestBC)
errAC <- sum((as.vector(pAC)-hTestAC$R)^2)/nrow(hTestAC)

p1 <- as.vector(predict(tAB, newdata = h))
p2 <- as.vector(predict(tBC, newdata = h))
p3 <- as.vector(predict(tAC, newdata = h))

p <- (p1/errAB+p2/errBC+p3/errAC)/(1/errAB+1/errBC+1/errAC)

p <- floor(p+.5)

length(which(p==h$R))/nrow(h)

## 75.4%

pAB <- floor(pAB+.5)
pBC <- floor(pBC+.5)
pAC <- floor(pAC+.5)

length(which(pAB==hTestAB$R))/nrow(hTestAB)
length(which(pBC==hTestBC$R))/nrow(hTestBC)
length(which(pAC==hTestAC$R))/nrow(hTestAC)

## Entre 67 y 71% de aciertos

# Probamos Bagging

library(ipred)
mb <- bagging(R ~ A + B + C + D + E, data=h, coob=TRUE)
pb <- predict(mb,newdata=h)
pb <- floor(.5+pb)
length(which(pb==h$R))/nrow(h) 

## Casi 80% mejor que bootstrap

# Para optimizar bagging par�metro nbag par�metro method


# Probamos Random Forest

library(randomForest)

rf <- randomForest(formula = R ~ A + B + C + D + E, data = h)

prf <- predict(rf, newdata=h)
prf <- floor(0.5+prf)

length(which(prf == h$R))/nrow(h)

## 94.3 % de aciertos, el mejor de la serie







