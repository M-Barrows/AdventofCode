def test_map_creation(map):
    assert map.start is not None
    assert map.target is not None
    print(map.target)

def test_map_target(map):
    assert map.target.position == [2,5]
    assert map.start.position == [0,0]

def test_map_size(map):
    print(map.grid)
    assert len(map.grid) == 40