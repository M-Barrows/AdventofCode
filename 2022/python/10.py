from aocd import get_data, submit
from typing import Any
from pprint import PrettyPrinter

test_input="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def get_cycle_actions(input:Any) -> int:
    register={1:1}
    current_cycle = 1
    for op in input:
        if len(op.split(' ')) == 1:
            current_cycle += 1
            register[current_cycle]=0 #noop
        else:
            current_cycle += 2
            register[current_cycle]=int(op.split(' ')[1])
    return register

if __name__ == '__main__':
    zip_data = lambda cycles,register: [(c,register) for c in cycles]
    cycle_signal_strength = lambda data: sum([v for (k,v) in data[1].items() if k <= data[0]]) * data[0]
    # Test Case
    test_output = get_cycle_actions(test_input.split('\n'))
    cycles = [20,60,100,140,180,220]
    print(sum(list(map(cycle_signal_strength,zip_data(cycles,test_output)))))

    d = get_data(day=10, year=2022)
    register_a = get_cycle_actions(d.split('\n'))
    a = sum(list(map(cycle_signal_strength,zip_data(cycles,register_a))))

    submit(a, part="a", day=10, year=2022)
    # submit(b, part="b", day=10, year=2022)
