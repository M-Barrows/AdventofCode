from aocd import get_data
from typing import Any

def get_solution(input:Any) -> tuple: 
    nested = [x.split('\n') for x in input]
    totals = [sum([int(y) for y in x]) for x in nested]
    a =max(totals)
    b = sum(sorted(totals,reverse=True)[:3])
    
    return a,b

if __name__ == '__main__':
    d = get_data(day=1, year=2022).split('\n\n')
    a,b = get_solution( input = d)
    print(a,b)