#"while" z "next"

iter <- 1
while (iter <= 10) {
  licznik <- sample(0:6, 1)
  mianownik <- sample(0:6, 1)
  if (mianownik == 0) {
    next
  }
  
  cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
  iter <- iter + 1
}

#"While" bez "next"

iter <- 1
while (iter <= 10) {
  licznik <- sample(0:6, 1)
  mianownik <- sample(0:6, 1)
  if (mianownik != 0) {
    cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
    iter <- iter + 1
  }
}

#"for" z "next"

for (iter in 1:10) {
  licznik <- sample(0:6, 1)
  mianownik <- sample(0:6, 1)
  if (mianownik == 0) {
    next
  }
  
  cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
}

#"for" bez "next"

for (iter in 1:10) {
  licznik <- sample(0:6, 1)
  mianownik <- sample(0:6, 1)
  if (mianownik != 0) {
    cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
  }
}
