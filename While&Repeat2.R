#przykład
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
}


