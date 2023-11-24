from aocd import get_data, submit
from typing import Any

def init_stacks(rows:list)->dict:
    stacks = {
        '1':[],
        '2':[],
        '3':[],
        '4':[],
        '5':[],
        '6':[],
        '7':[],
        '8':[],
        '9':[]
    }
    box_loc = list(range(2,35,4)) #char index of box label
    for i,x in enumerate(rows[:-1]):
        for j,y in enumerate(box_loc):
            if x[y-1] != ' ':
                stacks.get(str(j+1)).append(x[y-1])
            else:
                continue
    
    return stacks

def move_boxes(stacks, instructions):
    for i in range(0,int(instructions[0])):
        removed = stacks.get(instructions[1]).pop(0)
        stacks.get(instructions[2]).insert(0,removed)

def move_boxes_b(stacks_b, instructions):
    to_move = stacks_b.get(instructions[1])[:int(instructions[0])]
    for x in to_move[::-1]:
        stacks_b.get(instructions[2]).insert(0,x)
    del stacks_b.get(instructions[1])[:int(instructions[0])]



def get_solution(starting, moves) -> tuple: 
    
    boxes = [x for x in starting.split('][')]
    rows = [x.split('\n') for x in boxes]
    stacks = init_stacks(rows[0])
    stacks_b = init_stacks(rows[0])
    
    moves = [x.split(' ')[1:6:2] for x in moves.split('\n')] #[[amount, from to], ... ]
    # moves = [[int(y) for y in x] for x in moves]
    # print(stacks)
    for move in moves:
        move_boxes(stacks,move)
    # print(stacks)
    a = list()
    for k,v in stacks.items():
        a.append(v[0])
    a = ''.join(a)

    print(stacks_b)
    for move in moves:
        move_boxes_b(stacks_b,move)
    print(stacks_b)
    b = list()
    for k,v in stacks_b.items():
        b.append(v[0])
    b = ''.join(b)
    
    return a,b

if __name__ == '__main__':
    starting, moves = (x for x in get_data(day=5, year=2022).split('\n\n'))
    a,b = get_solution( starting = starting, moves = moves)
    print(a,b)
    submit(a, part="a", day=5, year=2022)
    submit(b, part="b", day=5, year=2022)