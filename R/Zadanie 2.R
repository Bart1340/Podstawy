Sum_Dice_Rolls <- 0   #ustawiamy sumę rzutów kostką na 0
Iteration_number <- 0   #ustawiamy liczbę iteracji na 0
while (Sum_Dice_Rolls<=1001) {   #dopóki suma rzutów kostką nie przekroczy 1000
  Iteration_number <- Iteration_number+1   #licznik iteracji 
  x <- sample(1:6,1)   #rzut kością sześciościenną
  Sum_Dice_Rolls <- Sum_Dice_Rolls+x  #Suma wszystkich rzutów 
}
print(Sum_Dice_Rolls)
print(Iteration_number)
