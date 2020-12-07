input <- read.csv('./Day5/input.csv',header = F,col.names = "seat",stringsAsFactors = F,strip.white = T)

parseSeats <- function(seatString){
  minRow <- 0
  maxRow <- 127
  rowLength <- 128
  minCol <- 0
  maxCol <- 7
  colLength <- 8
  row <- integer()
  col <- integer()
  for(letter in 1:6) {
    rowLength <- rowLength/2
    if (substr(seatString,letter,letter) == "F"){
      maxRow = minRow + rowLength
    }
    if (substr(seatString,letter,letter) == "B"){
      minRow = minRow + rowLength
    }
  }
  if(substr(seatString,7,7) == "F"){ row <- minRow} else {row <- maxRow}
  
  
  for(letter in 8:9){
    colLength <- colLength/2
    if (substr(seatString,letter,letter) == "L"){
      maxCol = minCol + colLength 
    }
    if (substr(seatString,letter,letter) == "R"){
      minCol = minCol + colLength 
    }
  }
  if(substr(seatString,10,10) == "L"){ col <- minCol} else {col <- maxCol+1}
  
  
  return((row-1)*8+col)
}

res<-cbind(input,seatID = sapply(as.array(input$seat),parseSeats))

#----- Part I Answer = 848 (still not correct code....)
max(res$seatID)

