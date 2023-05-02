iter <- 1
while (iter<=10) {
  licznik <- sample(0:6,1)
  mianownik <- sample(0:6,1)
  if (mianownik==0) {
    next
  }
  cat("Iteracja:",iter,"z ułamkiem",licznik,"/",mianownik,"==",licznik/mianownik,"\n")
  iter <- iter+1
}

for (iter in 1:10) {
  licznik <- sample(0:6,1)
  mianownik <- sample(0:6,1)
  if (mianownik==0) {
    next
  }
  cat("Iteracja:", iter, " z ułamkiem ", licznik, "/", mianownik, "==", licznik/mianownik, "\n")
}

#W przypadku, gdy mianownik jest równy "0" operator "next" 
#sprawia, że pętla "for" po prostu pomija daną interacje i przechodzi do następnej -
#dlatego nie jest wyświetlana i nie sumują się one do 10 
