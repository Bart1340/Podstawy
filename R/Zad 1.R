#Zad 1 - Silnia rekurencyjnie 
Silnia <- function(n){
  if (n==0) {
    return(1)
  }
  n*Silnia(n-1)
}

Silnia(5)





