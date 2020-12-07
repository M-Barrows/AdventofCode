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

#------Part II Answer = 160
inputdf %>%
  mutate(id = row_number()) %>%
  separate_rows(details,convert = T, sep = "\\s") %>%
  separate(details,c("key","value"),":") %>%
  filter(key != "cid" ) %>%
  spread(key,value) %>%
  select (-V1) %>% 
  mutate(
    validFields = 
      ifelse(nchar(byr)==4 & as.numeric(byr) >= 1920 & as.numeric(byr)  <= 2002,1,0)  #byr
      + ifelse(nchar(iyr)==4 & as.numeric(iyr) >= 2010 & as.numeric(iyr) <= 2020,1,0)  #iyr
      + ifelse(nchar(eyr)==4 & as.numeric(eyr) >= 2020 & as.numeric(eyr) <= 2030,1,0)  #eyr
      + ifelse(grepl("^1[5-8][0-9]cm|19[1-3]cm|59in|6[0-9]in|7[0-6]in$",hgt),1,0)  #hgt
      + ifelse(grepl("^#[0-9a-f]{6}$",hcl),1,0) #hcl 
      + ifelse(grepl("^amb|blu|brn|gry|grn|hzl|oth$",ecl),1,0) #ecl
      + ifelse(grepl("^[0-9]{9}$",pid),1,0) #pid
  ) %>%
  filter(validFields == 7) %>%
  select(byr,iyr,eyr,hgt,hcl,ecl,pid,validFields) %>%
  nrow()

