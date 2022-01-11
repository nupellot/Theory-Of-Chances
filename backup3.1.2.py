import matplotlib.pyplot as graph

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 27, 28, 22]

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.


# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]
p = l / m
A = [1] #       1 / 0!,      p / 1!,              p^2 / 2!,                p^3 / 3!,        p^4 / 4!, ...
P0 = [1] #      1 / 1,  1 / (1 + p),    1 / (1 + p + p^2 / 2!),  1 / (1 + p + p^2 / 2! + p^3 / 3!) ...
# A[i] * P0[i] = P[i]

sm = A[0]

for i in range(1, 100):
    A.append(A[-1] * p / i)
    sm += A[-1]
    P0.append(1 / sm)


def sumAn(n):
    res = 0
    for i in range(n + 1):
        res += A[i]
    return res


n = 12
k = 12

# Q[n][i] = A[n] * (p / n) ^ k
Q = [[0] * (n + 7) for i in range(n + 7)]
P0Q = [[0] * (n + 7) for i in range(n + 7)]


for i in range(n + 7):
    Q[i][0] = 1
    P0Q[i][0] = P0[i]

sm = 0
for i in range(1, n + 5):
    sm = sumAn(i)
    Q[i][0] = A[i]
    for j in range(1, n + 5):
        Q[i][j] = ((p / i) * Q[i][j - 1])
        sm += Q[i][j]
        P0Q[i][j] = 1 / sm


def sumQk(n, k):
    res = 0
    for i in range(1, k + 1):
        res += Q[n][i]
    return res


# P0[n] * (A[0] + A[1] + .. + A[n]) = 1
check = sumAn(5)
check *= P0[5]
print(f"check without queue work = {check}")

# P(n) = A[n] * P0[n]
check = sumAn(5)
check *= P0Q[5][0]
print(f"check without queue = {check}")

# P(n + k) = P0Q[n][k] * Q[n][k]
# P0Q[n][k] * (A[0] + A[1] + .. + A[n] +
#             (Q[n][1] + Q[n][2] + .. + Q[n][k])) = 1
# Q[n][k] = (p / n) ^ k * A[n]


check = sumAn(5)
check += sumQk(5, 3)
check *= P0Q[5][3]
print(f"check with queue: {check}")


def check(n, k):
    res = P0Q[n][k] * (sumAn(n) + sumQk(n, k))
    return res


print(f"check(n, k) = {check(5, 3)}")


# def que(n):
#     x = [i for i in range(1, n + 1)]
#     y = [Q[n][i] for i in x]
#     graph.title(f"L оч, n = {n}")  # заголовок
#     graph.xlabel("k")  # ось абсцисс
#     graph.ylabel("L")  # ось ординат
#     graph.grid()  # включение отображение сетки
#     graph.plot(x, y)
#     graph.show()
#     graph.legend()


def Potk(n):
    x = [i for i in range(k + 1)]
    y = [P0Q[n][i] * Q[n][i] for i in x]
    # y[0] = 1
    graph.title(f"P отк")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("P")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x, y, label=f"n={n}")
    graph.legend()


def Mzan1(n, k):
    res = 0
    for i in range(n + 1):
        res += i * P0Q[n][k] * A[i]
    for i in range(1, k + 1):
        res += n * P0Q[n][k] * Q[n][i]
    return res


def Mzan(k):
    x = [i for i in range(1, n + 1)]
    y = [Mzan1(i, k) for i in x]
    graph.title(f"M зан")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("M")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x, y, label=f"k = {k}")
    graph.legend()


def Kzagr1(n, k):
    return Mzan1(n, k) / n


def Kzagr(k):
    x = [i for i in range(1, n + 1)]
    y = [Kzagr1(i, k) for i in x]
    graph.title(f"K загр")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("K")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x, y, label=f"k = {k}")
    graph.legend()


def Pque1(n, k):
    res = 1
    for i in range(n + 1):
        res -= P0Q[n][k] * A[i]
    return res


def Pque(k):
    x = [i for i in range(n + 1)]
    y = [Pque1(i, k) for i in x]
    y[0] = 1
    graph.title(f"P оч")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("P")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x, y, label=f"k = {k}")
    graph.legend()


def MlenQ1(n, k):
    res = 0
    for j in range(1, k + 1):
        res += j * Q[n][j] * P0Q[n][k]
    return res


def MlenQ(k):
    x = [i for i in range(n + 1)]
    y = [MlenQ1(i, k) for i in x]
    # y[0] = 0
    graph.title(f"M длины очереди")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("M")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x[1:], y[1:], label=f"k = {k}")
    graph.legend()


def KzanQ1(n, k):
    return MlenQ1(n, k) / k


def KzanQ(k):
    x = [i for i in range(1, n + 1)]
    y = [KzanQ1(i, k) for i in x]
    # y[0] = 0
    graph.title(f"K занятости очереди")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("M")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.plot(x, y, label=f"k = {k}")
    graph.legend()


for i in range(1, k + 1):
    Potk(i)
graph.show()

for i in range(1, k + 1):
    Mzan(i)
graph.show()

for i in range(1, k + 1):
    Kzagr(i)
graph.show()

for i in range(1, k + 1):
    Pque(i)
graph.show()

for i in range(1, k + 1):
    MlenQ(i)
graph.show()

for i in range(1, k + 1):
    KzanQ(i)
graph.show()
