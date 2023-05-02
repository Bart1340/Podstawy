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
