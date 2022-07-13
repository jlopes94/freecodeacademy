class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __int__(self):
        return self.width, self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        counts = 0
        p = ""
        # if too big, skip and print response
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        else:
            p = ("*" * self.width + "\n") * self.height
        return p

    def get_amount_inside(self, shape):
        if self.get_area() < shape.get_area():
            return 0
        else:
            return int(self.get_area() / shape.get_area())


class Square(Rectangle):

    def __init__(self, side, width=None, height=None):
        super().__init__(width, height)
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_width(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_height(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

# dog = Square(4)
# print(dog.get_area())
