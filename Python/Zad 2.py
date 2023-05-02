#Ćwiczenie 2:
#1. Przygotujcie listę:
  #a. list_a = ['Kraków', 'Radom', '34', 512, 300, 'Szczecin', 'Gorzów']
import string

#2. Przygotujcie skrypt, który sprawdzi:
  #a. Czy dany element jest nazwą miasta czy liczbą
  #b. Jeśli jest nazwą miasta:
  #i. Dodajcie do niego przedrostek „m.' tak, żeby otrzymać formę np. „m. Kraków'
  #c. Jeśli jest liczbą:
  #i. Dodajcie do niej 15
  #d. Na koniec zapiszcie wyniki w formie zmodyfikowanej listy zawierającej nazwy miast z przedrostkami i powiększone liczby a następnie wyświetlcie tę listę na ekranie.

#1.
list_a = ['Kraków', 'Radom', '34', 512, 300, 'Szczecin', 'Gorzów']

modified_list = []
for n in list_a:
   if isinstance(n, str) and n.isalpha(): #sprawdza czy jest nazwą miasta (sprawdza czy to string i czy znaki są alfabetyczne)
       modified_list.append('m. '+n) #dodaje przedrostek
   elif isinstance(n, int or float): #sprawdza czy jest liczbą całkowitą lub rzeczywistą
       modified_list.append(n+15) #dodaje 15
   elif isinstance(n, str) and n.isnumeric(): #sprawdza przypadki, w których liczba została zapisana jako string
       modified_list.append(int(n)+15)
print(modified_list)










