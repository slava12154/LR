sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s
print("Максимальная площадь треугольника\n", smax)

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2-4*a*c
print('x1 = ', (-b - d**0.5)/2*a)
print('x2 = ', (-b + d**0.5)/2*a)


# git remote add origin
# git push -u origin main
# slava12154
# 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
# git commit -m "Find max square of triangles"
# token = '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'
# На вход программе подаются 3 коэффициента квадратного
# уравнения. Программа должна находить корни квадратного уравнения.
