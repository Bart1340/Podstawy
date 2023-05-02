#przykład 1: definiujemy serie - nowy typ obiektu określony w bibliotece Pandas

import pandas as pd
a = [2, 5, 8, 9]
b = pd.Series(a) #aplikujemy metodę w celu sformatowania listy 'a'
print(b)

#przykład 2: inny sposób na to samo

b = pd.Series([2, 5, 8, 9]) #aplikujemy metodę w celu sformatowania listy

print(b)

#przykład 3: Co możemy zrobić z seriami? - transformacje

c = b * 10 #szybkie transformacje obliczeniowe wykonywane dla całej serii
print(c)

#przykład 4: Co możemy zrobić z seriami? - statystyki opisowe

c = b.describe() #statystyki opisowe
print(c)
b.describe()

#przykład 5: import tabeli z danymi

df = pd.read_csv("C:/Users/Bartosz/Desktop/data1.csv")
print(df.to_string())

#przykład 6: komendy pandas - rozmiar zbioru

print(len(df))

#przykład 7: komendy pandas - przegląd jednej kolumny

print(df.age)

#przykład 8: Mediana dla zmiennej

print(df["height"].median())

#przykład 9: wylosujcie próbę ze zbioru o N=10

g = df.sample(n=10)
print(g.to_string())

#przykład 9: wyświetlcie 10 najstarszych rekordów

h = df.nlargest(10, 'age')
print(h.to_string())

#przykład 10: wyświetlcie 10 najniższych rekordów

j = df.nsmallest(10, 'height')
print(j.to_string())

#przykład 11: wybieramy określony zakres wierszy

k = df.iloc[2:45]
print(k.to_string())

#przykład 12: wybieramy określony zakres wierszy bazując na ich wartości

l = df.query('age > 30 and gender == "m"')
print(l.to_string())