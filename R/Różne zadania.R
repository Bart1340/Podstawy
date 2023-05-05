#Zad 1 - Silnia rekurencyjnie 
Silnia <- function(n){
  if (n==0) {
    return(1)
  }
  n*Silnia(n-1)
}

Silnia(5)

#Zad 2 - Silnia iteracyjnie 

Silnia <- function(n){
  Result <- 1
  if (n==0) {
    return(1)
  }
  for (i in seq(1, length=n)) {
    Result <- Result*i
  }
  print(Result)
}
Silnia(5)

#Zad 3 fibonacci rekurencyjnie 
Fibonacci <- function(n){
  if(n==0) {
    return(0)
  } else if(n==1) {
    return(1)
  } else {
    return(Fibonacci(n-1)+Fibonacci(n-2))
  }
}
Fibonacci(8)  

#Zad 4 fibonacci iteracyjnie 
Fibonacci <- function(n) {
  FibSequence <- c(1,1)
  if(n==0) {
    return(0)
  } else if(n==1) {
    return(1)
  } else if(n==2) {
    return(1)
  } else {
    for (i in seq(3,length=n)) {
      FibSequence[i] = FibSequence[i-1]+FibSequence[i-2]
    }
  }
  FibSequence[n]
}
Fibonacci(8)

#Zad 5
losuj_min_max <- function(n){
  my_matrix <- apply(matrix(nrow = n,ncol = n), 1:2, function(x) sample(1:6,1)+sample(1:6,1))
  print(my_matrix) #W każdej komórce macierzy n x n zostaje wpisana suma rzutu dwiema kostkami
  Max_Numbers <- apply(my_matrix, 2, max)
  print(Max_Numbers) #Podawana jest największa wartość w każdej kolumnie
  Min_Number <- min(Max_Numbers)#Z największych wartości wybierana jest najmniejsza 
  cat("Najmniejsza liczba to", Min_Number)
}

losuj_min_max(5)

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

#Zad 7
n <- 1
while (TRUE){
  n <- n+1
  if (n%%7==0 & n%%2==1 & n%%3==1 & n%%4==1 & n%%5==1 & n%%6==1) {
    cat(n,"-","to jest rozwiązanie zadania")
    break
  }
}



  


                     
                     
                  

    
    



