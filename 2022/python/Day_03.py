from aocd import get_data, submit
from typing import Any

from collections import Counter
import string

def split_list(lst:list) -> tuple:
    return lst[int(len(lst)/2):],lst[:int(len(lst)/2)]

def get_solution(input:Any) -> tuple: 
    lists = [split_list(x) for x in input]
    duplicates = [Counter(list[0]) & Counter(list[1]) for list in lists]
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    a = sum([letters.index(list(x)[0])+1 for x in duplicates])

    groups = [input[i:i+3] for i in range(0,len(input),3)]
    duplicates = [Counter(list[0]) & Counter(list[1]) & Counter(list[2]) for list in groups]
    b = sum([letters.index(list(x)[0])+1 for x in duplicates])
    return a,b

if __name__ == '__main__':
    d = get_data(day=3, year=2022).split('\n')
    a,b = get_solution( input = d)
    print(a,b)
    submit(a, part="a", day=3, year=2022)
    submit(b, part="b", day=3, year=2022)