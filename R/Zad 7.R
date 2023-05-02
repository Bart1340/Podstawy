#Zad 7
n <- 1
while (TRUE){
  n <- n+1
  if (n%%7==0 & n%%2==1 & n%%3==1 & n%%4==1 & n%%5==1 & n%%6==1) {
    cat(n,"-","to jest rozwiązanie zadania")
    break
  }
}

