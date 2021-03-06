import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 23]

a = 81
c = 17
m = 100
# n = [100, 5, 10, 25, 50]
X0 = B[1]
n = (100, *range(2, 101))
# print(*n)
def rand(previousX):
    return (a * previousX + c) % m

print('a =', a, 'c =', c, 'm =', m, 'X0 =', X0)
X = [X0]  # Массив сгенерированных чисел.
while True:
    X.append(rand(X[-1]))
    # Проверяем, не встречалось ли число ранее.
    isUnique = True
    firstAppearance = 0
    for i in range(0, len(X) - 1):
        if X[i] == X[-1]:
            isUnique = False
            firstAppearance = i
    # Выходим из цикла в случае, если число повторилось
    if (isUnique == False): break


# print(*X, sep = '\n')
for i in range(0, len(X)):
    # print(i, '->', X[i])
    if (i % 10 == 0): print()
    print('%2d' % X[i], end = ' ')
print('\nПериод:', len(X) - 1 - firstAppearance)

# Распределяем значения выданные генератором по значениям
collumns = [0] * 10
for i in range(0, 50):
    collumns[X[i] // 10] += 1



# Считаем Xi^2
r = len(collumns)
p = 1 / r
Xi2 = 0
for i in range(0, len(collumns)):
    Xi2 += (collumns[i] - n[-1] * p)**2 / (n[-1] * p)
v = r - 1
print('\nXi2:', Xi2, 'v:', v)


M = [0] * len(n)  # Выборочное среднее.
D = [0] * len(n)  # Смещенная выборочная дисперсия.
S = [0] * len(n)  # Исправленная выборочная дисперсия.

# Посчитаем все нужные величины для разных n
for i in range(0, len(n)):
    for j in range(0, n[i]):
        M[i] += 1 / n[i] * X[j]
    for j in range(0, n[i]):
        D[i] += 1 / n[i] * (X[j] - M[i])**2
    for j in range(0, n[i]):
        S[i] += 1 / (n[i] - 1) * (X[j] - M[i])**2
    print(n[i], '->', '[x]', '%.7d' % M[i], '[D]', '%.7d' % D[i], '[S^2]', '%.7d' % S[i])




# Выводим распределение значений выданных генератором
x = [i for i in range(0, r)]
y = [collumns[i] for i in x]
graph.title("Распределение значений выданных генератором")  # Название графика.
graph.xlabel("Номер интервала")  # Подпись оси абсцисс.
graph.ylabel("Кол-во значений в интервале")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()


x = [i for i in range(5, len(n))]
y = [D[i] for i in x]
graph.plot(x, y, label=f"D")
y = [S[i] for i in x]
graph.plot(x, y, label=f"S")
y = [D[0] for i in x]
graph.plot(x, y, label=f"D[100]")
graph.legend()
graph.title("")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("")  # Подпись оси ординат.
graph.grid()  # Включение отображения сетки.
graph.show()

y = [math.fabs(D[i] - S[i]) for i in x]
graph.plot(x, y, label=f"|D[n] - S[n]|")
graph.legend()
graph.title("")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("")  # Подпись оси ординат.
graph.grid()  # Включение отображения сетки.
graph.show()
