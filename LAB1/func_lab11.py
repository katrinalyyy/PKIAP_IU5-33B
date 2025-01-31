import math


def check(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("x принадлежит R")
        return True
    elif a == 0 and c == 0:
        print("x = 0")
        return True
    elif a == 0 and b == 0:
        print("Нет действительных корней")
        return True
    elif a == 0 and b != 0 and c != 0:
        # bx^2 = -c
        # x^2 = -c/b
        t = -c/b
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


# at^2+bt+c=0
def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D


def Solution_sqrt_equation(a, b, c):
    D = discriminant(a, b, c)
    if D > 0:
        t1 = (-b + math.sqrt(D))/(2*a)
        t2 = (-b - math.sqrt(D)) / (2 * a)
        return [t1, t2]
    elif D == 0:
        t = (-b)/(2*a)
        return [t]
    else:
        return []


def Rrturn_X(a, b, c):
    T_res = Solution_sqrt_equation(a, b, c)
    res = []
    for t in T_res:
        if t > 0:
            res.append(math.sqrt(t))
            res.append(-math.sqrt(t))
        elif t == 0:
            res.append(0)
    return res


def check_abc(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод. Введите число")


def main():
    a = check_abc("Введите коэффициент A: ")
    b = check_abc("Введите коэффициент B: ")
    c = check_abc("Введите коэффициент C: ")

    if check(a, b, c):
        return

    X_res = Rrturn_X(a, b, c)
    if X_res:
        print("Корни уравнения: ", *X_res)
    else:
        print("Нет действительных корней")


if __name__ == "__main__":
    main()