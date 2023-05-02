#ładowanie bioblioteki vioplot, zbiór danych iris i zmienna species_list

library(vioplot)
data(iris)
species_list <- lapply(levels(iris[["Species"]]),
                       function(x)
                         {iris[iris[, "Species"]==x, 1:4]
  })
names(species_list) <- levels(iris[["Species"]])

#kod do wykresów violinowych

for (i in 1:4) {
  data_ith_column <- lapply(species_list, function(x) x[[i]])
  vioplot(data_ith_column, main=colnames(iris)[i], col=palette.colors(palette = "Okabe-Ito")[2:4]) #Odpowiednie nagłówki i kolory
  if (i %in% c(3,4)){ #jeżeli jest na 3 albo 4 wykresie
    ypos=(min(data_ith_column$versicolor) - 0.1) #ypos mniejszy o 0,1 od najmniejszej wartości versicolor
    lines(c(0, 4), c(ypos,ypos), col="red", lty=2, lwd=0.2) #linia 
    text(3.5, ypos, paste("y=", ypos, sep=""), col="black", pos=3, cex=0.8) #tekst
  }
}
#boxplot
for (i in 1:4) {
  data_ith_column <- lapply(species_list, function(x) x[[i]])
  boxplot(data_ith_column, main=colnames(iris)[i], col=palette.colors(palette = "Okabe-Ito")[2:4]) #Odpowiednie nagłówki
  if (i %in% c(3,4)){ #jeżeli jest na 3 albo 4 wykresie
    ypos=(min(data_ith_column$versicolor) - 0.1) #ypos mniejszy o 0,1 od najmniejszej wartości versicolor
    lines(c(0, 4), c(ypos,ypos), col="red", lty=2, lwd=0.2) #linia 
    text(3.5, ypos, paste("y=", ypos, sep=""), col="black", pos=3, cex=0.8) #tekst
  }
}

