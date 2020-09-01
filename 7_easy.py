# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def ploshad(self):
        self.perimetr /=2
        self.ploshad =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.ploshad)

    def vysota(self):
        self.ploshad *=2
        self.vysota =  round((self.ploshad / self.CA),2)
        return (self.vysota)

my_tri = Triangle(0,0,0,4,4,0)

print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.ploshad()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.vysota()))

print(77*"_")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class trapezoid():
    def __init__(self, name, x1, y1, x2, y2, x3, y3, x4, y4):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    
    def __str__(self):
       return self.name
 
    def proverka(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
  
        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")
    
        
    def side(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)
        
    def perimeter(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return ( a+b+c+d)
    
    def area(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return  ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))
 
    
fis_trap = trapezoid('one', 0,0,2,2,4,2,6,0)
fis_trap.proverka()
fis_trap.side()
print("Периметр :"+str(fis_trap.perimeter()))
print("Площадь: " + str(fis_trap.area()))
fis_trap1 = trapezoid('two', 0,0,3,3,6,3,9,0)
fis_trap1.proverka()
fis_trap1.side()
print("Периметр: "+str(fis_trap1.perimeter()))
print("Площадь: " + str(fis_trap1.area()))
