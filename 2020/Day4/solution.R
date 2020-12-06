require(stringr)
require(tidyr)
require(dplyr)
input <- readChar('./Day4/input.csv',file.info('./Day4/input.csv')$size)
inputdf <- as.data.frame(str_split(input,"\n\n"),stringsAsFactors = F,col.names = "details")

#-----Part I Answer = 226
inputdf %>%
  mutate(id = row_number()) %>%
  separate_rows(details,convert = T, sep = "\\s") %>%
  separate(details,c("key","value"),":") %>%
  filter(key != "cid" ) %>%
  na.omit() %>%
  group_by(id) %>%
  summarise(fields = n()) %>%
  filter(fields == 7) %>%
  nrow()

