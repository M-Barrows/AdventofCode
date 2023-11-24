from aocd import get_data, submit
from typing import Any,List
import numpy as np
from dataclasses import dataclass, field




def find_start_location(grid):
    # Starting backwards due to shape of land 
    # Search input for 'E' 
    # Set height to 26
    # Save target coordinate
    return np.array([np.where(np.isin(grid,-28))[0][0],np.where(np.isin(grid,-28))[0][0],26])

def assign_heuristics(current:List[int,int,int],goal:List[int,int,int]):
    # assign a value for "closeness"
    return sum(abs(current[0] - goal[0]),abs(current[1]-goal[1]),abs(current[2]-goal[2])) # 3D Manhattan distance


def get_solution(input:Any,) -> int:
    a = None
    b = None
    pass
if __name__ == '__main__':
    lines = get_data(day=6, year=2022).split('\n')
    data = [[ord(letter)-97 for letter in line] for line in lines]

    print(a,b)
    submit(a, part="a", day=6, year=2022)
    submit(b, part="b", day=6, year=2022)
