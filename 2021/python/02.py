from aocd import get_data
from typing import Any

def get_solution(input:Any) -> tuple: 
    moves = [x.split(' ') for x in input]
    h = 0
    d = 0
    for move in moves: 
        h += int(move[1]) if 'forward' in move else 0
        d += int(move[1]) if 'down' in move else 0
        d += -1*int(move[1]) if 'up' in move else 0
    a = h*d

    h = 0
    d = 0
    a = 0
    for move in moves: 
        a += int(move[1]) if 'down' in move else 0
        a += -1*int(move[1]) if 'up' in move else 0
        if 'forward' in move: 
            h += int(move[1])
            d += (a*int(move[1]))
    b = h*d
    return a,b

if __name__ == '__main__':
    d = get_data(day=2, year=2021).split('\n')
    a,b = get_solution( input = d)
    print(a,b)