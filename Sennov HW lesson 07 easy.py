# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # def vector(p1, p2):
    #     return [int(i) - int(j) for i, j in zip(p1, p2)]
        def sidelen(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)**0.5
        self.ab = sidelen(self.a, self.b)
        self.bc = sidelen(self.b, self.c)
        self.ac = sidelen(self.a, self.c)
    def area(self):
        semi_perimeter = self.perim() / 2
 
        return (semi_perimeter * (semi_perimeter - self.ab) * (semi_perimeter - self.bc) * (semi_perimeter - self.ac))**0.5
    def height(self):
        return self.area() / (self.ab / 2)
    def perim(self):
        return self.ab + self.bc + self.ac
triangle1 = triangle((0, 0), (0, 3), (4, 0))
 
print(triangle1.area())
print(triangle1.height())
print(triangle1.perim())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class iso_trapez:
    def __init__ (self, a, b, c, d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        def sidelen(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)**0.5
        self.ab = sidelen(self.a, self.b)
        self.bc = sidelen(self.b, self.c)
        self.cd = sidelen(self.c, self.d)
        self.ad = sidelen(self.a, self.d)
        self.ac = sidelen(self.a, self.c)
        self.bd = sidelen(self.b, self.d)
        sides=[self.ab, self.bc, self.cd, self.ac]
        for i in range(4):
            if sides[i] == max(sides):
                self.base=sides[i]
                self.ceil=sides[i-2]
                self.leftside=sides[i-3]
                self.rightside=sides[i-1]
            
    def check(self):
        result=False
        if self.ac == self.bd and self.base != self.ceil:
            result=True
        else:
            print('Это не равнобедренная трапеция')
        return result
    def sidelengths(self):
        if self.check() == True:
            print(f'Длинны сторон: {round(self.ab, 2)}, {round(self.bc, 2)}, {round(self.cd, 2)}, {round(self.ad, 2)}')
    def perim(self):
        if self.check() == True:
            perimeter=round(self.ab + self.bc + self.cd + self.ad, 2)
            print(f'Периметр: {perimeter}')
    def area(self):
        if self.check() == True:
            semi_perimeter = self.perim()/2
            S = round(((semi_perimeter-self.base)*(semi_perimeter-self.ceil)*((semi_perimeter-self.leftside)**2))**0.5, 2)
            print(f'Площадь: {S}')


trapez1 = iso_trapez((1, 0), (5, 1), (6, 5), (0, 5))
trapez1.check() 
trapez1.sidelengths()
trapez1.perim()
trapez1.area()