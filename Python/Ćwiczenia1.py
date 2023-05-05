#Ćwiczenie 1 - funkcje

def fun_rename(osoba):
    print("abs." + osoba)

fun_rename("marcin")
fun_rename("Ola")
fun_rename("Aga")

#Ćwiczenie 2 - funkcje

def pole1(radius):
    pole=radius*2*3.14
    print(pole)

pole1(7)

#Ćwiczenie 3 - funkcje

def pole2(radius):
    ctrltype=type(radius)
    if ctrltype == int or ctrltype == float:
        pole=radius*2*3.14
        print(pole)
    else:
        print("invalid data type")

pole2(7)
pole2("t")

#Ćwiczenie 4 – funkcje z więcej niż jednym argumentem

def pole3(a,h):
    pole=1/2*a*h
    print(pole)

pole3(12,66)

#Ćwiczenie 5 - funkcje

def pole4(a,b,h):
    pole=1/2*(a+b)*h
    print(pole)

pole4(5,3,7)

#Ćwiczenie 6 - funkcje
#Zdefiniujcie samodzielnie funkcję, która z jedenastocyfrowego ciągu liczb obcina 3 skrajne z prawej (do walidacji długości polecam funkcję len())

def cut(list):
    return list[:-3]

list = (1,2,3,4,5,6,7,8,9,9,9,9,4,5,6,7)
cut(list)

def cut(list):
    if len(list) != 11:
        print("invalid length")
    else:
        return list[:-3]

ciąg = (1,2,3,4,5,6,7,8,9,9,9,3,4,5)
cut(ciąg)

#Ćwiczenie 7 - klasy

class sensor:
    def __init__(self, rawdata, thereshold):
        self.rawdata = rawdata
        self.thereshold = thereshold
    def transformata(self):
        print(self.rawdata - self.thereshold)

measurement = sensor(240, 50)
measurement.transformata()

#Ćwiczenie 8

class Robot:
    def __init__(self, url, liczba_calkowita, data):
        self.url = url
        self.liczba_calkowita = liczba_calkowita
        self.data = data

    def parse(self):
        if not isinstance(self.url, str):
            raise TypeError("Adres URL musi być ciągiem tekstowym.")
        if not self.url.startswith("https://"):
            raise ValueError("Adres URL musi zaczynać się od 'https://'")
        return self.url[8:]

r = Robot("https://www.example.com", 42, "2023-04-23")
r.parse()

#Ćwiczenie 9 - iteratory
lista = ["apple","banana","orange"]
myiter = iter(lista)
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Ćwiczenie 10 - iteratory
#1) Stwórzcie listę 10 słów
#2) Korzystając z pętli for, warunku if/else i iteratora sprawdźcie które ze słów zaczynają się na 'A' i wypiszcie je na ekranie

lista_slow = ["ananas", "arbuz", "banan", "cytryna", "daktyl", "eukaliptus", "figa", "gruszka", "herbata", "jabłko"]
for slowo in lista_slow:
    if slowo.startswith('a'):
        print(slowo)
    else:
        pass

#Ćwiczenie 11 – dostęp do pliku
#1) Otwieramy plik
#2) Pobieramy pierwszy element z pliku
#3) Zamykamy plik

with open("C:/Users/Bartosz/Desktop/data1.csv") as f:
    contents = f.readlines()
    iterator = iter(contents)
    print(next(iterator))

#Ćwiczenie 13 – dostęp do pliku
#1) utwórzcie plik z 12 aresami URL
#2) przygotujcie skrypt który otwiera plik, sprawdza które adresy zaczynają się od http:// a które od https://, policzcie ile jest URL każdego typu, a następnie zwróćcie:
#Liczbę URL z HTTPS
#Listę URL z HTTPS
#Liczbę URL z HTTP
#Listę URL z HTTP

with open("C:/Users/Bartosz/Desktop/adresy.txt") as plik:
    http_adresy = []
    https_adresy = []
    for adres in plik:
        if adres.startswith("http://"):
            http_adresy.append(adres.strip())
        elif adres.startswith("https://"):
            https_adresy.append(adres.strip())

liczba_http_adresow = len(http_adresy)
http_lista = http_adresy

liczba_https_adresow = len(https_adresy)
https_lista = https_adresy

print(f"Liczba adresów HTTP: {liczba_http_adresow}")

print(f"Lista adresów HTTP: {http_lista}")
print(f"Liczba adresów HTTPS: {liczba_https_adresow}")
print(f"Lista adresów HTTPS: {https_lista}")

