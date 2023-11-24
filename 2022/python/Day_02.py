from aocd import get_data, submit
from typing import Any

def get_solution(input:Any) -> tuple:
    points_a = {
    'A X': 4, 
    'A Y': 8, 
    'A Z': 3, 

    'B X': 1,
    'B Y': 5,
    'B Z': 9,

    'C X': 7,
    'C Y': 2,
    'C Z': 6
    }
    a = sum([points_a[x] for x in input])
    points_b = {
    'A X': 3, 
    'A Y': 4, 
    'A Z': 8, 

    'B X': 1,
    'B Y': 5,
    'B Z': 9,

    'C X': 2,
    'C Y': 6,
    'C Z': 7
    }
    b = sum([points_b[x] for x in input])
    return a,b

if __name__ == '__main__':
    d = get_data(day=2, year=2022).split('\n')
    a,b = get_solution( input = d)
    print(a,b)
    submit(a, part="a", day=2, year=2022)
    submit(b, part="b", day=2, year=2022)
