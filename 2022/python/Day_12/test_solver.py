from Models import Solver

def test_solver_creation(map):
    s = Solver(map)
    assert s.map is not None

def test_choose_neighbor(map):
    s = Solver(map)
    first = s.current_location
    s.choose_neighbor()
    second = s.current_location
    print(first,second)
    assert first != second
    assert len(s.current_path) == 2

def test_example_solution(map):
    s = Solver(map)
    while s.current_location != s.map.target:
        s.choose_neighbor()
        print(s.current_location)
    print([loc.position for loc in s.current_path])
    assert len(s.current_path) == 31