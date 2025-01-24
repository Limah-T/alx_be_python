import math

class Shape:
    def area(self):
        raise NotImplementedError("The derived classed need to override this method.")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        """Formula is πr2 where π=3.14159"""
        shape_area = math.pi * (self.length * self.length)
        return shape_area


