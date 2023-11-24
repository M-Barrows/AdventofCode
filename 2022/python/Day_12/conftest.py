import pytest
from pytest import fixture
from Models import Map,Location

@pytest.fixture
def test_input(): 
    text = """aabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    return text

@pytest.fixture
def location(position:list[int,int]=[20,21],height:int=12):
    return Location(position,height)

@pytest.fixture
def map(test_input):
    # locations = [
    #     Location([0,0],0),
    #     Location([0,1],0),
    #     Location([0,2],1),
    #     Location([0,3],16),
    #     Location([0,4],15),
    #     Location([0,5],14),
    #     Location([0,6],13),
    #     Location([0,7],12),

    #     Location([1,0],0),
    #     Location([1,1],1),
    #     Location([1,2],2),
    #     Location([1,3],17),
    #     Location([1,4],24),
    #     Location([1,5],23),
    #     Location([1,6],23),
    #     Location([1,7],11),

    #     Location([2,0],0),
    #     Location([2,1],3),
    #     Location([2,2],3),
    #     Location([2,3],18),
    #     Location([2,4],25),
    #     Location([2,5],26),
    #     Location([2,6],23),
    #     Location([2,7],10),

    #     Location([3,0],0),
    #     Location([3,1],3),
    #     Location([3,2],3),
    #     Location([3,3],19),
    #     Location([3,4],20),
    #     Location([3,5],21),
    #     Location([3,6],22),
    #     Location([3,7],9),
        
    #     Location([4,0],0),
    #     Location([4,1],1),
    #     Location([4,2],3),
    #     Location([4,3],4),
    #     Location([4,4],5),
    #     Location([4,5],6),
    #     Location([4,6],7),
    #     Location([4,7],8)
    # ]
    # return Solver(locations,locations[21],locations[0])
    return Map(test_input)