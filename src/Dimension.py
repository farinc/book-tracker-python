class Dimension: 

    def __init__(self, width: float = 0, height: float = 0):
        super().__init__()

        self._width: float = width
        self._height: float = height
    
    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def calculateArea(self) -> float:
        return self.height * self.width