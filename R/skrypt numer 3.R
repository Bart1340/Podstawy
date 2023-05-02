#wczytujemy biblioteki

library(tidyverse)

# wczytujemy dane sondażowe

NESdta <- read_csv("https://raw.githubusercontent.com/PTesta/PS230/master/anes_pilot_2016.csv")


# tworzymy nową ramkę danych  z danymi dotyczącymi wieku, przynależności partyjnej płci i temperatury postawy wobec Trumpa i Obamy

NESdta_sub <- NESdta %>% 
  dplyr::select(fttrump, pid3, birthyr, gender, ftobama) %>%
  mutate(age = (2016 - birthyr),
         fttrump = replace(fttrump, fttrump > 100, NA), 
         ftobama = replace(ftobama, ftobama == 998, NA), 
         Party = case_when(pid3 == 1 ~ "Democrat",
                           pid3 == 2 ~ "Republican", 
                           pid3 == 3 ~ "Independent"),
         gender2 = case_when(gender == 2 ~ "female", 
                             gender == 1 ~ "male",
                             gender == 0 ~ "none"),
         female = ifelse(gender == 2, 1, 0)) %>% 
  as.data.frame() %>% 
  drop_na()


# mikrozadanie 11

# proszę opisać działanie funkcji select(), mutate(),  case_when(), ifelse() oraz drop_na() w powyższym kodzie
#select - Wybiera kolumny 
#mutate - Tworzy nowe kolumny/Zmienia stare kolumny
#case_when - Jeżeli kolumna przyjmuje jakąś wartość to...
#ifelse 
#drop_na

# mikrozadanie 12 proszę narysować wykres ilustrujący relację 
#między wiekiem wyborców a temperaturą uczuć wobec Donalda Trumpa (NESdta_sub) 
#jak można zinterpretować ten wykres?

attach(NESdta_sub)

ggplot(NESdta_sub,aes(x=age,y=fttrump))+
  geom_point()+
  geom_smooth()

ggplot(NESdta_sub,aes(x=age,y=fttrump))+
  geom_point()+
  geom_smooth(method = lm)

ggplot(NESdta_sub,aes(x=age,y=ftobama))+
  geom_point()+
  geom_smooth()

#mikrozadanie 13 jak płeć i party id wyjaśniają  temperaturę uczuć wobe trumpa 

lm(formula = fttrump ~ age, NESdta_sub)
lm(formula = fttrump ~ gender2  + Party, NESdta_sub)

regresja1 <- lm(formula = fttrump ~ age, NESdta_sub)
summary(regresja1)

regresja2 <- lm(formula = fttrump ~ gender2  + Party, NESdta_sub)
summary(regresja2)
