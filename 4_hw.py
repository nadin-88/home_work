#1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_square (self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width+ self.height)

Rect1 = Rectangle (5, 4)
Rect2 = Rectangle (3,1)
Rect3 = Rectangle (9,10)

print(f"Площадь 1 прямоугольника: {Rect1.calculate_square()}")
print(f"Периметр 1 прямоугольника: {Rect1.calculate_perimeter()}\n")

print(f"Площадь 2 прямоугольника: {Rect2.calculate_square()}")
print(f"Периметр 2 прямоугольника: {Rect2.calculate_perimeter()}\n")

print(f"Площадь 3 прямоугольника: {Rect3.calculate_square()}")
print(f"Периметр 3 прямоугольника: {Rect3.calculate_perimeter()}\n")

#2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition (self):
        return self.a + self.b
    def multiplication (self):
        return self.a * self.b
    def divition(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b

Math1 = Math(25,12)
print(f"addition: {Math1.addition()}")
print(f"multiplication: {Math1.multiplication()}")
print(f"divition: {Math1.divition()}")
print(f"subtraction: {Math1.subtraction()}")


#3
class Button:
    def __init__(self, text, loc =""):
        self.text = text
        self.loc = loc
    def click(self):
        return f"Клик по кнопке {self.text}"
buttons = [
    Button ('Text Box'),
    Button ('Check box'),
    Button ('Radio button'),
    Button ('Web tables'),
    Button ('Web tables'),
    Button ('Buttons'),
    Button ('Links'),
    Button ('Broken links-Images'),
    Button ('Upload and Download'),
    Button ('Dynamic properties')
]
for button in buttons:
    print(button.text)
for button in buttons:
    print(button.click())

#4
class Car:
    def __init__(self):
        self.color = None
        self.type = None
        self.year = None
    def start(self):
        print("Автомобиль заведен")
    def stop(self):
        print (" Автомобиль заглушен")
    def set_year(self, year):
        self.year = year
        print(f'Год выпуска {year}')
    def set_type(self,car_type):
        self.type = car_type
        print(f'Тип машины {car_type}')

    def set_color(self, color):
        self.color = color
        print(f'Цвет машины {color}')
my_car = Car()

my_car.set_color('yellow')
my_car.set_type('Mazda')
my_car.set_year(2020)

my_car.start()
my_car.stop()
