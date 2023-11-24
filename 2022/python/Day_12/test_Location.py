import pytest
from Models import Location

def test_location_populated():
    l = Location(height=23,position=[0,12])
    assert l.height == 23
    assert l.position == [0,12]

def test_location_negative_height():
    with pytest.raises(ValueError):
        l = Location(height=-2,position=[0,12])

def test_missing_arguments():
    with pytest.raises(TypeError):
        l = Location(height=2)

def test_missing_arguments():
    with pytest.raises(ValueError):
        l = Location(position=[2,12])

def test_set_distance_to_target():
    l = Location(height=23,position=[0,12])
    l.distance_to_target = 13
    assert l.distance_to_target == 13
    l = Location(height=23,position=[0,12],distance_to_target=13)
    assert l.distance_to_target == 13