from aocd import get_data, submit
from typing import Any, List
from pprint import PrettyPrinter

test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

# history = ['/','/a/','/a/b']
# dir_sizes= {'/':123, '/a/': 345, ...}
# commands = [['ls','dir a','123 py.sh'],['cd a']]

def group_commands(input) -> List[str]:
    input_list = input.split('\n$ ')
    input_list = [x.split('\n') for x in input_list]
    return input_list[1:]

def cd(new_dir:str,history:list) -> List:
    if new_dir == '..':
        history = history[:-1]
    else:
        history.append(new_dir)
    return history

def ls(contents:list,history:list,dir_sizes:dict) -> None:
    total_size = sum([int(file.split(' ')[0]) for file in contents if file.split(' ')[0] != 'dir'])
    for i,_ in enumerate(history,start=1):
        path = '/'.join(history[:i])[1:]
        path = '/' if path == '' else path
        if dir_sizes.get(path,None) == None:
            dir_sizes[path] = 0
        dir_sizes[path] += total_size

def get_solution(input:Any) -> tuple:
    dir_sizes = {'/':0}
    history = ['/']
    commands = group_commands(input)
    for command in commands:
        if command[0][:2] == 'cd':
            history = cd(command[0].split(' ')[1],history)
        else:
            ls(command[1:],history,dir_sizes)
    a = sum([v for (k,v) in dir_sizes.items() if v <= 100_000])
    
    # Part B 
    needed_space = 30_000_000 - (70_000_000 - dir_sizes.get('/'))
    b = min([v for (k,v) in dir_sizes.items() if v > needed_space])
    return a,b

test_results = get_solution(test_data) 
assert test_results == (95437,24933642)

d = get_data(day=7,year=2022)
a,b= get_solution(d)
submit(a, part="a", day=7, year=2022)
submit(b, part="b", day=7, year=2022)