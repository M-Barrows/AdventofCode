from dataclasses import dataclass, field

@dataclass
class Location:
    position:list[int,int]
    height:int 
    distance_to_target:int = field(default=None)
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value not in range(27):
            raise ValueError(f'Attempting to set height outside normal limits [0,27): {value}')
        self._height = value


@dataclass
class Map: 
    __input_string: str
    start: Location = field(default = Location([0,0],0))
    target: Location = field(default = None)
    grid: list[Location] = field(default_factory=list)
    

    def __post_init__(self):
        self.grid = self.__load_map_from_input(input=self.__input_string)
        self.target = self.__get_target(self.grid)
        self.__calculate_distances()

    def __calculate_distances(self):
        for i,location in enumerate(self.grid):
            self.grid[i].distance_to_target = abs(location.position[0]-self.target.position[0]) + abs(location.position[1]-self.target.position[1])
            print(self.grid[i])
        self.start=self.grid[0]

    def __load_map_from_input(self,input:str):
        _map = []
        lines = input.split('\n')
        for i,line in enumerate(lines): 
            for j,location in enumerate(line): 
                height = 26 if ord(location)-97 == -28 else ord(location)-97
                l = Location([i,j],height)
                _map.append(l)
        return _map

    def __get_target(self,locations:list[Location],target_height:int = 26):
        return [location for location in locations if location.height == target_height][0]

@dataclass
class Solver:
    map: Map
    current_path: list = field(default_factory=list)
    current_location: Location = field(default=None)
    paths: list[dict] = field(default_factory=list)

    def __post_init__(self):
        self.current_location = self.map.start
        self.current_path.append(self.current_location)


    def __get_manhattan_distance(self,p1:list[int,int],p2:list[int,int]):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def get_neighbors(self):
        self.current_location.position
        return [location for location in self.map.grid if self.__get_manhattan_distance(self.current_location.position,location.position)==1]

    def choose_neighbor(self):
        for neighbor in sorted(self.get_neighbors(),key=lambda x: x.distance_to_target):
            if neighbor in self.current_path:
                continue
            if neighbor.height - self.current_location.height > 1:
                continue
            else:
                self.current_location = neighbor
                self.current_path.append(self.current_location)
                if self.current_path[-1] in self.paths:
                    self.paths[self.paths.index(self.current_path[-1])] = self.current_path
                else:
                    self.paths.append(self.current_path)

