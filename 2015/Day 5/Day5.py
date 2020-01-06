import csv 
import string
import re

# Read input data
words = open('2015/Day 5/input.csv').read().splitlines()

# Define functions
def vowelCount(word):
    count = 0
    count += word.count('a')
    count += word.count('e')
    count += word.count('i')
    count += word.count('o')
    count += word.count('u')
    return count

doubles = []
for i in list(string.ascii_lowercase): 
    doubles.append(i*2)


def doublesPresent(word):
    for i in doubles:
        if i in word:
            return True
    return False

def naughtyStrings(word):
    for i in ['ab','cd','pq','xy']:
        if i in word:
            return True
    return False

# Calculate Results
nice = 0
for word in words:
    if vowelCount(word) >= 3 and doublesPresent(word) == True and naughtyStrings(word) == False:
        nice += 1
print(nice)



for word in words:
    print(re.findall(['aeiou'],str))