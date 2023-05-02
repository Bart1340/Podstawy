#ćwiczenie 1: Przygotujcie listę dni tygodnia

import pandas as pd
Dni_Tygodnia = pd.Series(["Pon","Wto","Śro","Czw","Pią","Sob","Nie"])
print(Dni_Tygodnia)

#ćwiczenie 2: Obliczcie pola kół dla których promieniami są elementy listy b
b = pd.Series([2, 5, 8, 9])

c=3.14*b**2
print(c)

#ćwiczenie 3: stwórzcie przykładową tabelę z danymi w MS excell i wyeksportujcie ją jako CSV a następnie zaimportujcie w skrypcie. Jakie problemy zaobserwowaliście?

data = pd.read_csv("C:/Users/Bartosz/Desktop/Marketing/ifood_df.csv")
print(data.to_string())

#Ćwiczenie 4: Użyjcie komendy 'describe' do opisu  jednej z kolumn

df = pd.read_csv("C:/Users/Bartosz/Desktop/data1.csv")
df["age"].describe()

#Ćwiczenie 5: Użyjcie komendy 'describe' do opisu  wszystkich kolumn

df.describe()

#Ćwiczenie 6: obliczcie osobną funkcją wariancję dla tych zmiennych dla których można to zrobić

df["age"].median()
df["height"].median()

#ćwiczenie 7: utwórzcie obiekty klasy dataframe osobno dla wszystkich mężczynz powyżej 30 rż i kobiet poniżej 30 rż i obliczcie statstyki opisowe dla obu tych grup osobno

M = df.query('gender == "m" and age>30')
DFM = pd.DataFrame(M)
DFM
DFM.describe()

K = df.query('gender == "k" and age<30')
DFF = pd.DataFrame(K)
DFF
DFF.describe()