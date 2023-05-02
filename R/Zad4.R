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

#Tutaj też nie jestem do końca pewien, jaka jest różnica 
#Pętla "while" sprawdza za każdym razem, czy warunek jest prawdziwy i rozpoczyna się tylko wtedy, gdy tak jest.
#Natomiast pętla "repeat" za pomocą "if" sprawdza, czy warunek jest nieprawdziwy i jeżeli tak, to przerywa pętle za pomocą "break".

