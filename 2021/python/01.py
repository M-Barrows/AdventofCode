from aocd import get_data
from typing import Any

def get_solution(input:Any) -> tuple: 
    a = sum([input[i-1]<x if i>0 else False for i,x in enumerate(input)])
    b = sum([sum(input[i-3:i])<sum(input[i-2:i+1]) if i>2 else False for i,_ in enumerate(input)])
    return a,b

if __name__ == '__main__':
    d = get_data(day=1, year=2021).split('\n')
    a,b = get_solution( input = [int(_) for _ in d])
    print(a,b)