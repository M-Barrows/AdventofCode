from aocd import get_data, submit
from typing import Any
import os
import math
from dataclasses import dataclass, field

@dataclass
class Monkey:
    name: str
    items: field(default_factory=list)
    operation_formula: str
    test_denominator: int
    true_target: str
    false_target: str
    total_inspects:int = 0

    def inspect(self):
        old = self.items[0]
        self.items[0] = eval(self.operation_formula)
        self.total_inspects += 1

    def reset_worry_level_strategy(self,val:str,lcm:int):
        if val=='a':
            self.items[0] = math.floor(self.items[0]/3)
        if val=='b': #Credit to @hannahilea for their assistance on part B. https://github.com/hannahilea/AOC_2022/blob/main/Days/Day_11/src/Day_11.jl
            self.items[0] = self.items[0]%lcm
    
    def test(self):
        test_remainder = self.items[0]%self.test_denominator
        return test_remainder == 0

    def throw_to_monkey(self,target_monkey:str,troupe:list[dataclass]):
        _item = self.items.pop(0)
        m = [monkey for monkey in troupe if monkey.name == target_monkey][0]
        m.items.append(_item)

    def process_items(self,troupe:list[dataclass],strategy:str,lcm:int):
        while len(self.items)>0:
            self.inspect()
            self.reset_worry_level_strategy(strategy,lcm)
            test_result = self.test()
            target = self.true_target if test_result else self.false_target
            self.throw_to_monkey(target,troupe)
            self.process_items(troupe,strategy,lcm)
    


with open(f'{os.path.dirname(os.path.realpath(__file__))}/11_test_input.txt','r') as f:
        test_input = f.read()

def parse_input(input):
    monkeys = input.split('\n\n') # Group by monkeys
    monkeys = [monkey.split(':\n') for monkey in monkeys] # Create List of details for each monkey
    monkey_dict = {monkey[0].split(' ')[1]:[str.strip(x).split(': ') for x in monkey[1].split('\n')] for monkey in monkeys} # clean up white space in details

    monkey_dict_empty = {}
    for monkey, details in monkey_dict.items():
        monkey_dict_empty[monkey] = {characteristic[0]: characteristic[1] for characteristic in details}

    monkey_dict = monkey_dict_empty
    
    for monkey, details in monkey_dict.items(): 
        monkey_dict[monkey]['items'] = [int(x) for x in monkey_dict[monkey]['Starting items'].split(', ')]
        monkey_dict[monkey]['operation_formula'] = monkey_dict[monkey]['Operation'].split('new = ')[1]
        monkey_dict[monkey]['test_denominator'] = int(monkey_dict[monkey]['Test'].split(' ')[-1])
        monkey_dict[monkey]['true_target'] = monkey_dict[monkey]['If true'].split(' ')[3]
        monkey_dict[monkey]['false_target'] = monkey_dict[monkey]['If false'].split(' ')[3]
        # Cleanup
        del monkey_dict[monkey]['If true']
        del monkey_dict[monkey]['If false']
        del monkey_dict[monkey]['Starting items']
        del monkey_dict[monkey]['Operation']
        del monkey_dict[monkey]['Test']
    [v.update({'name':k}) for k,v in monkey_dict.items()]
    monkey_list = [v for k,v in monkey_dict.items()]
    lcm = math.prod([monkey['test_denominator'] for monkey in monkey_list])
    return monkey_list, lcm
### Operations for eval()

### Solution Synthesis
def get_solution(troupe:list,rounds:int,worry_reset_strategy:str,lcm:int) -> int:
    for i in range(0,rounds):
        for monkey in troupe:
            monkey.process_items(troupe,worry_reset_strategy,lcm)
    top_monkeys = [monkey.total_inspects for monkey in sorted(troupe,key = lambda monkey: -monkey.total_inspects)[:2]]
    return top_monkeys[0] * top_monkeys[1]

if __name__ == '__main__':
    monkey_list_a,lcm_a = parse_input(test_input)
    test_troupe_a = [Monkey(**monkey) for monkey in monkey_list_a]
    test_result = get_solution(test_troupe_a,20,'a',lcm_a)
    assert 10605 == test_result
    print('Passed tests for part A!')
    
    d = get_data(day=11, year=2022)
    monkey_list_a,lcm_a = parse_input(d)
    troupe_a = [Monkey(**monkey) for monkey in monkey_list_a]
    result_a = get_solution(troupe_a,10_000,'a',lcm_a)
    submit(result_a, part="a", day=11, year=2022)
    
    monkey_list_b,lcm_b = parse_input(test_input)
    test_troupe_b = [Monkey(**monkey) for monkey in monkey_list_b]
    test_result_b = get_solution(test_troupe_b,10_000,'b',lcm_b)
    assert 2713310158 == test_result_b
    print('Passed tests for part B!')

    d = get_data(day=11, year=2022)
    monkey_list_b,lcm_b = parse_input(d)
    troupe_b = [Monkey(**monkey) for monkey in monkey_list_b]
    result_b = get_solution(troupe_b,10_000,'b',lcm_b)
    submit(result_b, part="b", day=11, year=2022)
    