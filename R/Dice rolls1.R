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

Sum_Dice_Rolls <- 0   #ustawiamy sumę rzutów kostką na 0
Iteration_number <- 0   #ustawiamy liczbę iteracji na 0
while (Sum_Dice_Rolls<=1001) {   #dopóki suma rzutów kostką nie przekroczy 1000
  Iteration_number <- Iteration_number+1   #licznik iteracji 
  x <- sample(1:6,1)   #rzut kością sześciościenną
  Sum_Dice_Rolls <- Sum_Dice_Rolls+x  #Suma wszystkich rzutów 
}
print(Sum_Dice_Rolls)
print(Iteration_number)
