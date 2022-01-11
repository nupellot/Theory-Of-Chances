import matplotlib.pyplot as graph

R = [2, 8, 11, 5]
G = [1, 10, 6, 10]
B = [2, 9, 11, 7]
RGB = [5, 27, 28, 22]

callPerios = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.


# Интенсивности потоков.
l = 1 / callPerios  # Лямбда. [к/с]
m = 1 / servicePeriod  # Мю. [к/с]

ratio = l / m
ratioExtents = [1] #       1,      ratio,              ratio^2,                ratio^3,        ratio^4, ...
p = [1] #      1 / 1,  1 / (1 + ratio),    1 / (1 + ratio + ratio^2), ...

# Ищем p.
denominator = ratioExtents[0]
for i in range(1, 20):
    ratioExtents.append(ratioExtents[-1] * ratio / i)
    denominator += ratioExtents[-1]
    p.append(1 / denominator)

n = 0
while ratioExtents[n] * p[n] > 0.01:
    n += 1
print(n)


def otk(n):
    x = [i for i in range(n + 1)]
    y = [ratioExtents[i] * p[i] for i in x]
    graph.title("P отк")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("P")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.bar(x, y)
    graph.show()


B = []


def busy(n):
    x = [i for i in range(n + 1)]
    y = []
    for i in x:
        sm = 0
        for j in range(i + 1):
            sm += ratioExtents[j] * p[i] * j
        B.append(sm)
    graph.title("M зан")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("M")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.bar(x, B)
    graph.show()


def zagr(n):
    x = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        B[i] /= i
    graph.title("K загр")  # заголовок
    graph.xlabel("n")  # ось абсцисс
    graph.ylabel("K")  # ось ординат
    graph.grid()  # включение отображение сетки
    graph.bar(x, B)
    graph.show()


otk(n)
busy(n)
zagr(n)