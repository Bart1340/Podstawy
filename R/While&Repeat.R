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

#3przykład
x <- 0
warunek_logiczny <- TRUE
while(warunek_logiczny) {
  x <- sample(1:6, 1)
  print(x)
  if (x==6) {
    warunek_logiczny <- FALSE
  }
}

x <- 0
warunek_logiczny <- TRUE
repeat {
  if (!warunek_logiczny) {
    break
  }
  x <- sample(1:6, 1)
  print(x)
  if (x==6) {
    warunek_logiczny <- FALSE
  }
