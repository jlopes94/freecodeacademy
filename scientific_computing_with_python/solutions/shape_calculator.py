class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        f"""Rectangle(width={self.width}, height={self.height})"""
        return

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
        # if small enough to not have empty space, print easily
        if self.height <= 2:
            while counts < self.height:
                p += ("*" * self.width) + "\n"
                counts += 1
            return print(p)
        elif self.width <= 2:
            while counts < self.height:
                p += ("*" * self.width) + "\n"
                counts += 1
            return print(p)
        # otherwise, print with respect to empty spaces
        else:
            wdots = "*" * self.width
            hdots = "*" + (' ' * (self.width - 2)) + "*"
            # print top width line
            p += wdots + "\n"
            # print height lines
            while counts + 2 < self.height:
                p += hdots + "\n"
                counts += 1
            # print bottom width line
            p += wdots
            return print(p)

    # def get_amount_inside(self):
    # how many times a shape could fit inside of this rectangle. a rectangle with a width of 4 and a height
    # of 8 could fit in two squares with sides of 4.


#  first arg width, second height
dog = Rectangle(4, 4)

print(dog.get_picture())

# class Square:
