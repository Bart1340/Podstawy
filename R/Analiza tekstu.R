#wczytujemy biblioteki


#################################################################################################################

# wczytujemy dane z twittera Trumpa

id <- "15hMN1d_-6wpmx8NnE50Q5URFDVsh-O7L"

trump <- read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id))

#wczytujemy biblioteki

library(tidyverse)
library(stopwords)
library(tidytext)
library(tm)
library(spacyr)
library(wordcloud)
library(RColorBrewer)
library(wordcloud2)

# tworzymy funkcję czyszczącą

clean_tweets <- function(x) {
  x %>% 
    str_remove_all(" ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)") %>%
    str_remove_all("@[[:alnum:]_]{4,}") %>%
    str_remove_all("#[[:alnum:]_]+") %>%
    str_replace_all("&amp;", "i") %>%
    str_remove_all("[[:punct:]]") %>%
    str_remove_all("^RT:? ") %>%
    str_replace_all("\\\n", " ") %>%
    str_remove_all("#\\w+") %>%
    str_remove_all(pattern = '[:emoji:]') %>%
    str_trim("both") %>%
    str_to_lower()
}

clean_tweets(trump['text'])
Tweet_Text <- clean_tweets(trump['text'])

#używając biblioteki tm obliczmy frekwencję słów i używając biblioteki worcloud stwórzmy chmurę słów

Corpus_Tweets <- Corpus(VectorSource(Tweet_Text))

Corpus_Tweets <- tm_map(Corpus_Tweets, removePunctuation)
Corpus_Tweets <- tm_map(Corpus_Tweets, removeWords, stopwords("english"))

Word_Frequency <- DocumentTermMatrix(Corpus_Tweets)

Word_Freq <- colSums(as.matrix(Word_Frequency))
Sorted_Freq <- sort(Word_Freq,decreasing = TRUE)
Sorted_Freq

wordcloud(Corpus_Tweets, min.freq = 10, max.words = 150, random.order = FALSE, scale = c(4, 0.5))
