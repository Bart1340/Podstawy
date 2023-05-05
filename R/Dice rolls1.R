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


