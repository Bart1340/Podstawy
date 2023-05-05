######################################################################
## analiza eksploracyjna c.d.  + podstawy analizy ekspalanacyjnej ####
######################################################################


# biblioteki 
library(tidyverse)

# dane do dzisiejszych zajęć

# dane panteon

id <- "15xCXZ-LzVs32KK6y-8liToTFuq82onPO"
panteon <- read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id),stringsAsFactors = TRUE)
attach(panteon)

#dane o PKB krajów i populacji z 2017 roku

kraje  <- read.csv2(file = url("https://raw.githubusercontent.com/Tomasz-Olczyk/testowe-repozytrium/main/kraje2017.csv"))



# mikrozadanie 7: policzmy korelację między PageViewsEnglish i PageViewsNonEnglish w danych panteon

Cor <- cor(PageViewsEnglish,PageViewsNonEnglish)
cor.test(PageViewsEnglish,PageViewsNonEnglish)
P_value <- 0.00000000000000022

# mikrozadanie 8: narysujmy wykres ukazujący korelację z zadania 7 niech wykres zawiera krzywą i adnotacje z wartością R i p

plot.default(PageViewsEnglish,PageViewsNonEnglish)

Cor <- cor(PageViewsEnglish,PageViewsNonEnglish)
cor.test(PageViewsEnglish,PageViewsNonEnglish)
P_value <- 0.00000000000000022
ggplot(panteon, aes(x=PageViewsEnglish,y=PageViewsNonEnglish))+
  geom_point()+
  geom_smooth()+
  annotate("text",x=max(PageViewsEnglish-2500000),y=min(PageViewsNonEnglish),label=Cor)+
  annotate("text",x=max(PageViewsEnglish-2500000),y=min(PageViewsNonEnglish+3000000),label=P_value)
  

# mikrozadanie 9: narysujmy wykres najlepiej pokazujący różnice rozkładu TotalPageViews według płci

ggplot(panteon, aes(x=gender,y=TotalPageViews, fill=gender))+
  geom_boxplot()+
  coord_cartesian(ylim = c(0,20000000))
  

#mikrozadanie 10: sprawdźmy jak suma wyświetleń postaci z danego kraju  
#(TotalPageViews) dla kraju koreluje z populacją i pkb tego kraju (zbiór kraje)

panteon$countryName<- str_to_title(panteon$countryName)
panteon$countryName

Joined <- left_join(kraje,panteon, by = c("kraj" = "countryName"))
attach(Joined)
Page_Views_Per_Country <- aggregate(Joined$TotalPageViews, by=list(Joined$kraj),FUN = sum)
Population_PKB_Country <- Joined[,2:4]      

Final <- left_join(Population_PKB_Country,Page_Views_Per_Country, by = c("kraj" = "Group.1"))
Final <- unique(Final)
colnames(Final)[4] <- "TotalPageViews"
attach(Final)

cor.test(TotalPageViews,populacja)
cor.test(TotalPageViews,PKB)


