require(tidyr)
require(dplyr)
require(stringr)

#-----Data Ingest--------
input<-read.csv("./Day2/input.csv",sep = "\n",header = F,col.names = "reps")

inputClean<- input %>% 
  separate(reps,c("reps","pwd"),": ") %>%
  separate(reps,c("reps","letter")," ") %>%
  separate(reps,c("min","max"),"-") %>%
  mutate(pwd = str_trim(pwd))

#------Part I Answer = 542-------
inputClean %>%
  mutate(
    count = str_count(pwd,letter),
    min = as.integer(min),
    max = as.integer(max)
  ) %>%
  filter(count >= min & count <= max) %>%
  nrow()

#----Part II Answer = 360-------
inputClean %>%
  rename(
    "pos1"=min,
    "pos2"=max
  ) %>%
  mutate(pos1Match = ifelse(substr(pwd,pos1,pos1)==letter,1,0),
         pos2Match = ifelse(substr(pwd,pos2,pos2)==letter,1,0),
         matchStrength = pos1Match + pos2Match
         ) %>%
  filter(matchStrength == 1) %>%
  nrow()
