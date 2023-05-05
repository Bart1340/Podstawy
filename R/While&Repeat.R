#1 przykład 
x <- 0
while(TRUE){
  x <- x+1
  print(x)
  if(x==4){
    break
  }
}

x <- 0
repeat {
  x <- x+1
  print(x)
  if(x==4){
    break
  }
}

#2 przykład
x <- 0
while(TRUE){
  x <- sample(1:6,1)
  print(x)
  if(x==6){
    break
  }
}

x <- 0
repeat {
  x <- sample(1:6,1)
  print(x)
  if(x==6){
    break
  }
}


