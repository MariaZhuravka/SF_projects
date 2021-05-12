from rectangle import Rectangle, Square, Circle

#далее создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#создаем 2 квардрата
square_1 = Square(5)
square_2 = Square(10)

# создаем круг
crcl_1= Circle(4)


figures = [rect_1, rect_2, square_1, square_2, crcl_1]
for figure in figures:
    if isinstance (figure, Square):
        print(figure.get_area_square())
    elif isinstance (figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())