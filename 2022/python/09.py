from aocd import get_data, submit
from typing import Any
import numpy as np

test_input="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

tail_ajustments = {
    '0,0':[0,0],
    '1,0':[0,0],
    '0,1':[0,0],
    '1,1':[0,0],

    '-2,1':[-1,1],
    '2,1':[1,1],
    '2,-1':[1,-1],
    '-2,-1':[-1,-1],


    '-1,2':[-1,1],
    '1,2':[1,1],
    '1,-2':[1,-1],
    '-1,-2':[-1,-1],


    '2,0':[1,0],
    '-2,0':[-1,0],

    '0,2':[0,1],
    '0,-2':[0,-1],
}

def move(knot,dir):
    knot[1] += 1 if dir == 'U' else 0
    knot[1] -= 1 if dir == 'D' else 0
    knot[0] += 1 if dir == 'R' else 0
    knot[0] -= 1 if dir == 'L' else 0
    return knot
    

def tail_too_far(head:list,tail:list) -> None:
    if abs(head[0] - tail[0]) == 2 and head[1] - tail[1] == 0:
        return True
    if abs(head[1] - tail[1]) == 2 and head[0] - tail[0] == 0:
        return True
    if abs(head[1] - tail[1]) == 1 and abs(head[0] - tail[0]) == 2:
        return True
    if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 2:
        return True
    return False

def adjust_tail(head:list,tail:list):
    adjustment_key = f"{head[0]-tail[0]},{head[1]-tail[1]}"
    tail = list(np.array(tail) + np.array(tail_ajustments.get(adjustment_key)))
    return tail
    


def get_solution(input:Any) -> int:
    head_pos = [0,0]
    tail_pos = [0,0]
    tail_visited=[[0,0]]
    instructions = [x.split(' ') for x in input.split('\n')]

    for instruction in instructions:
        for _ in range(0,int(instruction[1])):
            head_pos = move(head_pos,instruction[0])
            if tail_too_far(head_pos,tail_pos):
                tail_pos = adjust_tail(head_pos,tail_pos)
            if tail_pos not in tail_visited:
                tail_visited.append(tail_pos)
    a,b = (len(tail_visited), None)
    return a,b

if __name__ == '__main__':
    test_a,test_b = get_solution(test_input)
    print(test_a)
    assert test_a == 13
    d = get_data(day=9, year=2022)
    a,b= get_solution(d)
    print(a,b)
    submit(a, part="a", day=9, year=2022)
    # submit(b, part="b", day=6, year=2022)
