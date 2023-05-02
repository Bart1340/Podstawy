#Zad 5
losuj_min_max <- function(n){
  my_matrix <- apply(matrix(nrow = n,ncol = n), 1:2, function(x) sample(1:6,1)+sample(1:6,1))
  print(my_matrix) #W każdej komórce macierzy n x n zostaje wpisana suma rzutu dwiema kostkami
  Max_Numbers <- apply(my_matrix, 2, max)
  print(Max_Numbers) #Podawana jest największa wartość w każdej kolumnie
  Min_Number <- min(Max_Numbers)#Z największych wartości wybierana jest najmniejsza 
  cat("Najmniejsza liczba to", Min_Number)
}

losuj_min_max(5)


#Wektor zawierający 1000 losowań z tego rozkładu - Nie do końca rozumiem to polecenie


