##########################################
# eksploracja danych  ####################
##########################################


#biblioteki

install.packages("tidyverse")
library(tidyverse)
install.packages("ggthemes")
library(ggthemes)

# dane

id <- "15xCXZ-LzVs32KK6y-8liToTFuq82onPO"
panteon <- read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id),stringsAsFactors = TRUE)


# notacja standardowa

options(scipen=999)


# zadanie 1. 
#stwórzmy wykres punktowy zależności między zmiennymi hwy i cyl zze zbioru danych mpg

?mpg
view(mpg)
attach(mpg)
plot(hwy,cyl)

ggplot(mpg,aes(x=hwy,y=cyl))+
  geom_point()

# zadanie 2:  Ile kobiet o imieniu Maria we wszystkich możliwych wersjach (takżę Marie, MArija itp) znajduje się w zbiorze Panteon?

maria <- subset(panteon, gender=="Female" & grepl("(^maria$|^maria\\b|\\bmaria\\b|\\bmarija\\b|\\bmari\\b|\\bmary\\b|\\bmarie\\b|\\bmariam\\b|\\bmariama\\b|\\bmariami\\b)", tolower(name)))
maria2 <- maria[-c(5068,9174,9277,9406,10681,10745,10836,10941),]
num_maria <- nrow(maria)
print(num_maria)

# zadanie 3: proszę podać trzy kraje z których pochodzi najwięcej kobiet o imieniu Maria ze zbioru Panteon

ggplot(maria, aes(x = num_maria,)) +
  geom_bar()+
  facet_wrap(~countryName)

maria_table <- table(maria$countryName)
sorted_maria_table <- sort(maria_table, decreasing = TRUE)
top_three_countries <- head(names(sorted_maria_table), 3)
print(top_three_countries)
  
# zadanie 4: narysujmy wykres porównujący liczbę kobiet i mężczyzn w podziale na kontynenty

attach(panteon)
my_colors <- c("#E69F00", "#56B4E9")
ggplot(panteon, aes(x = gender, fill = gender)) +
  geom_bar() +
  facet_wrap(~continentName) +
  scale_fill_manual(values = my_colors)


# zadanie 5: narysujmy wykres porównujący liczbę wyświetleń (totalPageViews) biografii kobiet z Polski
options(scipen = 999)
attach(panteon)
panteon2 <- panteon[countryName=="Poland" & gender=="Female" | countryName=="POLAND" & gender=="Female",]

ggplot(panteon2,aes(x=TotalPageViews, y=name))+
  geom_col()
# zadanie 6: określmy relaywną popularność kobiet i mężczyzn w domenach (domain), jak można pokazać to porównanie na wykresie?








