for (i in 1:100) {  #Dla każdej kolejnej iteracji "i" aż do 100
  dice_rolls_to_sum <- i-1   #rzuty kostką do zsumowania o 1 mniejsze od liczby iteracji
  sum <- 0 #  Na początku każdej iteracji sumę rzutów ustawiamy na 0 
  if (dice_rolls_to_sum >= 1) {   #Jeżeli liczba rzutów do zsumowania jest większa od 0
    for (dice_roll in 1:dice_rolls_to_sum) {  #Dla każdego kolejnego rzutu kostką w zbiorze rzutów do zsumowania
      if((i %% 2) == 0)  #Jeżeli liczba iteracji jest parzysta to rzut kostką dwunastościenną 
        x <-  {sample(1:12,1)
        } else   #Jeżeli liczba iteracji jest nieparzysta to rzut kostką sześciościenną 
          x <- {sample(1:6,1)
          }  
        sum <- sum + x   #Suma rzutów kostką w danej iteracji      
    }
  }
  cat("Iteracja",i,"-","suma rzutów",sum, "\n")
}