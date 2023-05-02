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
