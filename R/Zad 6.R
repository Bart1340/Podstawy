#Zad 6
Silnia <- function(n){
    if (n==0) {
      return(1)
    }
    n*Silnia(n-1)
}

dwumian_newtona <- function(n,k){
  Silnia(n)/(Silnia(k)*Silnia(n-k))
}
dwumian_newtona(6,4)



  


