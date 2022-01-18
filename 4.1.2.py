import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 23]

a = 81
c = 17
m = 100
n = 50
X0 = B[1]

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
    print(i, '->', X[i])
print('Период:', len(X) - 1 - firstAppearance)

# Распределяем значения выданные генератором по значениям
collumns = [0] * 10
for i in range(0, n):
    collumns[X[i] // 10] += 1

# Выводим распределение значений генератора
x = [i for i in range(0, 10)]
y = [collumns[i] for i in x]
graph.title("Распределение значений выданных генератором")  # Название графика.
graph.xlabel("Номер интервала")  # Подпись оси абсцисс.
graph.ylabel("Кол-во значений в интервале")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()


# Считаем Xi^2
r = len(collumns)
p = 1 / r
Xi2 = 0
for i in range(0, len(collumns)):
    Xi2 += (collumns[i] - n * p)**2 / (n * p)
v = r - 1
print('Xi2:', Xi2, 'v:', v)
