input <- read.csv('./Day1/input.csv',sep = '\n',col.names = 'input')
#----------------
soln <- data.frame(input)
soln$compliment <- (2020-soln$input)
soln$product <- (soln$input * soln$compliment)

#Part I answer = 1007104
soln[soln$compliment %in% soln$input,"product"][1]
#----------------

inputAsc <- sort(input$input,decreasing = F)
inputDesc <- sort(input$input,decreasing = T)

# Part II answer = 18847752
for (i in 1:length(inputDesc)) {
  for(j in 1:length(inputAsc)) {
    if((2020-inputDesc[i]-inputAsc[j]) %in% inputAsc){
      print(inputDesc[i] * inputAsc[j] * (2020-inputDesc[i]-inputAsc[j]))
    }
    else{next}
  }
}
