import math

class BiQuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            print("x принадлежит R")
            return True
        elif self.a == 0 and self.c == 0:
            print("x = 0")
            return True
        elif self.a == 0 and self.b == 0:
            print("Нет действительных корней")
            return True
        elif self.a == 0 and self.b != 0 and self.c != 0:
            t = -self.c / self.b
            if t > 0:
                x1 = math.sqrt(t)
                x2 = -math.sqrt(t)
                res = [x1, x2]
            elif t == 0:
                x = math.sqrt(t)
                res = [x]
            else:
                print("Нет действительных корней")
            print("Корни уравнения: ", *res)
            return True
        return False

    def discriminant(self):
        return self.b**2 - 4 * self.a * self.c

    def Solution_sqrt_equation(self):
        D = self.discriminant()
        if D > 0:
            t1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            t2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            return [t1, t2]
        elif D == 0:
            t = -self.b / (2 * self.a)
            return [t]
        else:
            return []

    def Rrturn_X(self):
        T_res = self.Solution_sqrt_equation()
        res = []
        for t in T_res:
            if t > 0:
                res.append(math.sqrt(t))
                res.append(-math.sqrt(t))
            elif t == 0:
                res.append(0)
        return res

    def solve(self):
        if self.check():
            return
        x_res = self.Rrturn_X()
        if x_res:
            print("Корни уравнения:", *x_res)
        else:
            print("Нет действительных корней")


class InputHandler:
    def check_abc(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Некорректный ввод. Введите число")


def main():
    a = InputHandler.check_abc("Введите коэффициент A: ")
    b = InputHandler.check_abc("Введите коэффициент B: ")
    c = InputHandler.check_abc("Введите коэффициент C: ")
    equation = BiQuadraticEquation(a, b, c)
    equation.solve()


if __name__ == "__main__":
    main()
