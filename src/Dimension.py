class Dimension: 

    def __init__(self, width: int, height: int):
        super().__init__()

        self.width: int = width
        self.height: int = height
    
    @property
    def width(self) -> int:
        return self.width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self.height

    @height.setter
    def height(self, value: int):
        self._height = value

    def calculateArea(self):
        return self.height * self.width