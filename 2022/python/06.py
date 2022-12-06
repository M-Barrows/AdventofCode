from aocd import get_data, submit
from typing import Any
from collections import Counter

def get_solution(input:Any, unique_sequence:int) -> int:
    for i,x in enumerate(input):
        if len(list(Counter(input[i:i+unique_sequence]))) == unique_sequence:
            return i+unique_sequence

if __name__ == '__main__':
    d = get_data(day=6, year=2022)
    a,b= (get_solution(d,4), get_solution(d,14))
    print(a,b)
    submit(a, part="a", day=6, year=2022)
    submit(b, part="b", day=6, year=2022)
