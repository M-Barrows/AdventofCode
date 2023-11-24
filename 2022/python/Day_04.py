from aocd import get_data, submit
from typing import Any

from collections import Counter

def zone_contains_other_zone(lst0,lst1):
    lst0 = range(int(lst0[0]),int(lst0[1])+1)
    lst1 = range(int(lst1[0]),int(lst1[1])+1)
    intersection = list(Counter(lst0) & Counter(lst1))
    return 1 if intersection == list(lst0) or intersection == list(lst1) else 0

def zones_overlap(lst0,lst1):
    lst0 = range(int(lst0[0]),int(lst0[1])+1)
    lst1 = range(int(lst1[0]),int(lst1[1])+1)
    intersection = list(Counter(lst0) & Counter(lst1))
    return 1 if len(intersection) > 0 else 0

def get_solution(input:Any) -> tuple: 
    d = [ [y.split('-') for y in x.split(',')] for x in input]
    a = sum([zone_contains_other_zone(i[0],i[1]) for i in d])
    b = sum([zones_overlap(i[0],i[1]) for i in d])
    return a,b

if __name__ == '__main__':
    d = get_data(day=4, year=2022).split('\n')
    a,b = get_solution( input = d)
    print(a,b)
    submit(a, part="a", day=4, year=2022)
    submit(b, part="b", day=4, year=2022)