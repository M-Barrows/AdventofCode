require(stringr)
require(dplyr)
#-----
input<- read.csv('./Day3/input.csv',header = F, col.names = 'rep1',stringsAsFactors = F,strip.white = T)

#-----Part I Answer = 262

input %>%
  mutate(
    strPosToRead = 3*(row_number()-1)+1,
    stripeWidth = str_length(input[1,1]),
    strRepsNeeded = ceiling(strPosToRead/stripeWidth),
    tree = ifelse(substr(strrep(rep1,strRepsNeeded),
                                     strPosToRead,strPosToRead) == "#",1,0)
  ) %>%
  summarise(sum(tree))

#-----Part II Answer = 2698900776
paths <- data.frame(matrix(c(1,1,3,1,5,1,7,1,1,2),nrow = 5,byrow = T))
colnames(paths) <- c("right","down")
for (i in 1:nrow(paths)){
  right <- paths[i,1]
  down <- paths[i,2]
  paths[i,"trees"] <- input %>%
    mutate(
      strPosToRead = right * (row_number()-1)+1,
      stripeWidth = str_length(input[1,1]),
      strRepsNeeded = ceiling(strPosToRead/stripeWidth),
      tree = ifelse(substr(strrep(rep1,strRepsNeeded),
                           strPosToRead,strPosToRead) == "#" & ((row_number() + 1) %% down) == 0,1,0)
    ) %>%
    summarise(sum(tree))
}
prod(paths$trees)
