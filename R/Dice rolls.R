###1
Dice_rolls <- 0      #ustawiamy liczbę rzutów na 0 
while (Dice_rolls<100){     #dopóki liczba rzutów jest mniejsza od 100 to:
  Dice_rolls <- Dice_rolls+1    #licznik rzutów 
  y <- sample(1:12,1)     #rzut kostką dwuanstościenną -y
  x <- sample(1:6,1)      #rzut kostką sześciościenną -x
  if (x>y) {      #jeżeli x>y to "x", jeżeli x równa się y to "remis", a jeżeli y>x to "y"
    print("x")
  } else if (x==y) {
    print("remis")
  } else {
    print("y")
  }
} 

###2
Sum_Dice_Rolls <- 0   #ustawiamy sumę rzutów kostką na 0
Iteration_number <- 0   #ustawiamy liczbę iteracji na 0
while (Sum_Dice_Rolls<=1001) {   #dopóki suma rzutów kostką nie przekroczy 1000
  Iteration_number <- Iteration_number+1   #licznik iteracji 
  x <- sample(1:6,1)   #rzut kością sześciościenną
  Sum_Dice_Rolls <- Sum_Dice_Rolls+x  #Suma wszystkich rzutów 
}
print(Sum_Dice_Rolls)
print(Iteration_number)


###3
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
