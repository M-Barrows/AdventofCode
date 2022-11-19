from aocd import get_data
from typing import Any
import pandas as pd


def get_solution(input:Any) -> tuple: 

    # Part 1
    df = pd.DataFrame([[bit for bit in number] for number in input])
    print(df.describe())
    gamma = ''.join(df.describe().loc['top'])
    epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
    a = int(gamma,2) * int(epsilon,2)

    # Part 2
    b= None
    return a,b

if __name__ == '__main__':
    d = get_data(day=3, year=2021).split('\n')
    a,b = get_solution( input = d)
    print(a,b)