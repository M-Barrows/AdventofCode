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
long_test = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

delta_adjustments = {
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

    '2,2':[1,1],
    '-2,-2':[-1,-1],
    '2,-2':[1,-1],
    '-2,2':[-1,1],
}

def move(knot,dir):
    knot[1] += 1 if dir == 'U' else 0
    knot[1] -= 1 if dir == 'D' else 0
    knot[0] += 1 if dir == 'R' else 0
    knot[0] -= 1 if dir == 'L' else 0
    return knot
    

def knot_too_far(head:list,tail:list) -> None:
    if abs(head[0] - tail[0]) == 2 and head[1] - tail[1] >= 0:
        return True
    if abs(head[1] - tail[1]) == 2 and head[0] - tail[0] >= 0:
        return True
    if abs(head[1] - tail[1]) >= 1 and abs(head[0] - tail[0]) == 2:
        return True
    if abs(head[0] - tail[0]) >= 1 and abs(head[1] - tail[1]) == 2:
        return True
    return False

def adjust_knot(head:list,tail:list):
    adjustment_key = f"{head[0]-tail[0]},{head[1]-tail[1]}"
    tail = list(tail + np.array(delta_adjustments.get(adjustment_key)))
    return tail

def get_solution(input:Any,num_knots) -> int:
    knot_pos = np.full((num_knots,2),0,int)
    tail_visited=[[0,0]]
    instructions = [x.split(' ') for x in input.split('\n')]

    for instruction in instructions:
        for _ in range(0,int(instruction[1])):
            knot_pos[0] = move(knot_pos[0],instruction[0])
            for i in range(1,num_knots):
                if knot_too_far(knot_pos[i-1],knot_pos[i]):
                    knot_pos[i] = adjust_knot(knot_pos[i-1],knot_pos[i])
            if list(knot_pos[num_knots-1]) not in tail_visited:
                tail_visited.append(list(knot_pos[num_knots-1]))
    a = len(tail_visited)
    return a

if __name__ == '__main__':
    test_a = get_solution(test_input,2)
    print(test_a)
    assert test_a == 13
    test_b = get_solution(test_input,10)
    print(test_b)
    assert test_b == 1
    test_c = get_solution(long_test,10)
    print(test_c)
    assert test_c == 36
    d = get_data(day=9, year=2022)
    a= get_solution(d,2)
    b = get_solution(d,10)
    print(a,b)
    submit(a, part="a", day=9, year=2022)
    submit(b, part="b", day=9, year=2022)
