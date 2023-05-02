#Ćwiczenie 1:
#1. Przygotujcie dwie listy:
  #a. list_a = ['Jan', 'Kowalski', '82010302345', '450', '23', '16', '18']
  #b. list_b = ['Jan', 'Kowalski', '82010302345', 231, 45, 26, 23]

#2. Przygotujcie skrypt który sprawdzi:
  #a. Czy obie listy dotyczą tej samej osoby (porównajcie imię, nazwisko i nr PESEL)
  #b. Jeśli tak to niech zsumują cztery ostatnie wartości z każdej z list, tworząc nową listę,
  # zawierającą imię, nazwisko, pesel oraz liczby będące sumami kolejnych elementów list

list_a = ['Jan', 'Kowalski', '82010302345', '450', '23', '16', '18']
list_b = ['Jan', 'Kowalski', '82010302345', 231, 45, 26, 23]

if list_a[0:3]==list_b[0:3]: #porównanie trzech pierwszych elementów
    print("Listy dotyczą tej samej osoby")
else:
    print("Listy nie dotyczą tej samej osoby")

if list_a[0:3]==list_b[0:3]:
    x= [int(list_a[-4]), int(list_a[-3]), int(list_a[-2]), int(list_a[-1])] #Stworzenie listy "x", w której 4 ostatnie wartości z listy "a" zostają zamienione na liczby całkowite
    y= list_b[-4:] #Stworzenie listy "y", która zawiera cztery ostatnie wartości z listy "b"
    Lista = [list_a[0],list_a[1], list_a[2], x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3]] #Stworzenie listy, która zawiera imię, nazwisko i pesel oraz sumę poszczególnych wartości z obu list
    print(Lista)

