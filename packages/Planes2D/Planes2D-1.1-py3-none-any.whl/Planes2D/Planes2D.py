class Plane():
    def __init__(self, deafult_value: int = 0) -> None:
        self.cells = []
        self.deafult_value = deafult_value
    
    def remove_cell(self, cell) -> None:
        if cell in self.cells:
            self.cells.remove(cell)

    def delete_empty(self) -> None:
        for cell in self.cells:
            if cell.value == 0:
                self.cells.remove(cell)
    
    def __getitem__(self, indices) -> object:
        index_x, index_y = indices
        for cell in self.cells:
            if cell == (index_x, index_y):
                return cell
        return Cell(self, 
                    index_x, 
                    index_y, 
                    value=self.deafult_value)

    def __str__(self) -> str:
        return "2DPlane Plane"
    
    def __repr__(self) -> str:
        if self.deafult_value == 0:
            return f"Plane()"
        else:
            return f"Plane(deafult_value={self.deafult_value})"

class Cell():
    def __init__(self, 
                 root: Plane, 
                 x: int, 
                 y: int, 
                 value: int = 1) -> None:
        self.value = value
        self._x = x
        self._y = y
        self._coords = (self._x, self._y)
        self._root = root
        self._empty = [(self._x-1, self._y+1),
                       (self._x, self._y+1),
                       (self._x+1, self._y+1),
                       (self._x-1, self._y),
                       (self._x+1, self._y),
                       (self._x-1, self._y-1),
                       (self._x, self._y-1),
                       (self._x+1, self._y-1)]
        if self not in self._root.cells:
            self._root.cells.append(self)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Cell):
            checks = (self._coords == __value.coords 
                     and self._root == __value.root)
            if checks and self.value != __value.value:
                raise ValueError("Two cells that appear to be equivalent have diffrent values")
            return checks
        elif isinstance(__value, tuple):
            return self._coords == __value
        else:
            return False

    def __str__(self) -> str:
        return f"2DPlane Cell: {self._coords}, value: {self.value}"
    
    def __repr__(self) -> str:
        if self._root.deafult_value == 0:
            deafult_value = ""
        else:
            deafult_value = "deafult_value=" + self._root.deafult_value
        
        if self.value == 1:
            return f"Cell(Plane({deafult_value}), {self._x}, {self._y})"
        else:
            return f"Cell(Plane({deafult_value}), {self._x}, {self._y}, value={self.value})"

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def coords(self):
        return self._coords
    @property
    def root(self):
        return self._root
    @property
    def empty(self):
        return self._empty