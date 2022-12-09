from aocd import get_data, submit
from typing import Any
import numpy as np

test_input = """30373
25512
65332
33549
35390"""

def prep_data(input:str) -> object: 
    grid = np.array([[int(y) for y in x] for x in input.split('\n')])
    print(grid)
    return grid
 
def find_visibility(grid):
    visibility_list = np.full(grid.shape,False,bool)
    for i,x in np.ndenumerate(grid):
        if min(i) == 0 or i[0] == grid.shape[0]-1 or i[1] == grid.shape[1]-1:
            visibility_list[i[0],i[1]] = True
        elif x > max(grid[i[0],:i[1]]) or x > max(grid[i[0],i[1]+1:]):
            visibility_list[i[0],i[1]] = True
        elif x > max(grid[:i[0],i[1]]) or x > max(grid[i[0]+1:,i[1]]):
            visibility_list[i[0],i[1]] = True
        else: 
            continue
    return visibility_list

def find_first_equal_or_larger_tree(trees)-> int:
    score = 0
    for i,tree in np.ndenumerate(trees): 
        if i[0] == 0:
            continue
        if tree >= trees[0]:
            score += 1
            break
        else:
            score += 1
    return score       

def find_scenic(grid):
    scenic_list = np.full(grid.shape,0,int)
    for i,x in np.ndenumerate(grid):
        left = find_first_equal_or_larger_tree(grid[i[0],i[1]::-1])
        right = find_first_equal_or_larger_tree(grid[i[0],i[1]:])
        up = find_first_equal_or_larger_tree(grid[i[0]::-1,i[1]])
        down = find_first_equal_or_larger_tree(grid[i[0]:,i[1]])
        scenic_list[i[0],i[1]]= left * right * up * down
    return scenic_list

def get_solution(input:Any) -> tuple:
    #Part A
    grid = prep_data(input)
    visibility_grid = find_visibility(grid)
    print(visibility_grid)
    a = len(sum(np.where(visibility_grid == True)))
    
    #Part B
    scenic_grid = find_scenic(grid)
    print(scenic_grid)
    b=scenic_grid.max()
    return a,b

if __name__ == '__main__':
    test_a,test_b = get_solution(test_input)
    assert test_a == 21
    assert test_b == 8
    d = get_data(day=8, year=2022)
    a,b= get_solution(d)
    print(a,b)
    submit(a, part="a", day=8, year=2022)
    submit(b, part="b", day=8, year=2022)
