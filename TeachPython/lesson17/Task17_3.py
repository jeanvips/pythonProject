class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square

    #Информация о цвете фигуры
    def info_color(self):
        print(f"Цвет фигуры: {self.color}")

    # Информация о площади фигуры
    def info_square(self):
        print(f"Площадь фигуры: {self.square} ед. изм.²")

    #Установить цвет фигуры
    def set_color(self):
        shape_color = str(input("Введите цвет: "))
        self.color = shape_color
        self.info_color()

    # Установить площадь фигуры
    def set_square(self):
        shape_square = int(input("Введите площадь: "))
        self.square = shape_square
        self.info_square()

s = Shape("Прозрачный", 0)
s.set_color()
s.set_square()