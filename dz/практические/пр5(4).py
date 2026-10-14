import math
def calculate_rectangle_area(width, height):

    return width*height

def calculate_circle_area(radius):

    return math.pi * radius ** 2

width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))
n= calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника: {n:.2f}")

radius = float(input("Введите радиус круга: "))
a = calculate_circle_area(radius)
print(f"Площадь круга: {a:.2f}")
