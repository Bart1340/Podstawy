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

for (iter in 1:10) {
  licznik <- sample(0:6, 1)
  mianownik <- sample(0:6, 1)
  if (mianownik == 0) {
    next
  }
  
  cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
}

#W przypadku pętli "for" w iteracjach, w których mianownik==0,"next" rozpoczyna pętle od nowa i przesuwa zmienną "iter" w wektorze o 1.
#Pętla po prostu przechodzi do następnej iteracji, zanim zdąży dojść do końca polecenia - dlatego wypisane iteracje nie sumują się do 10.
#W przypadku pętli "while" skrypt działa, dopóki licznik iteracji wynosi <=10. 
#W momencie, gdy kod dojdzie do "next"i mianownik==0,"while" przeprowadza walidacje warunku i rozpoczyna nową iterację. 
#Żeby "iter <- iter +1" (licznik iteracji) zwiększył się o 1, to pętla musi przejść do samego końca - dlatego wypisane iteracje sumują się do 10.
