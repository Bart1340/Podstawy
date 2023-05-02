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

  
    
    