class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f"{self.__width:.1f}cm"

    @property
    def height(self):
        return f"{self.__height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)