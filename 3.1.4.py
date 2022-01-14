import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 27, 28, 22]

OPS = 13  # Вычисленное в прошлом пункте число операторов. Выступает верхней границей в данном пункте.

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.
waitingTime = RGB[1] + RGB[2] + RGB[3]  # Среднее время ожидания в очереди.

# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]
p = l / m  # Загрузка системы.
v = 1 / waitingTime  # Ожидание.
eps = 10**-2

queueLength = 5

probs = [[] for i in range(0, OPS)]  # Все возможные вероятности.
# Считаем все возможные вероятности.
for n in range(1, OPS):
    while True:
        probs[n].clear()
        queueLength += 1
        denominator = 0
        for i in range(0, n + 1):
            denominator += p**i / math.factorial(i)

        # summ = 0
        for i in range(1, queueLength + 1):
            multiplication = 1
            for j in range(1, i + 1):
                multiplication *= (n * m + j * v)
            denominator += l**(n + i) / (m**n * math.factorial(n) * multiplication)
        # denominator += summ

        p0 = 1 / denominator
        probs[n].append(p0)
        for i in range(1, n + 1):
            probs[n].append(p0 * p**i / math.factorial(i))
        for i in range(1, queueLength + 1):
            multiplication = 1
            for j in range(1, i + 1):
                multiplication *= (n * m + j * v)
            probs[n].append(p0 * l**(i + n) / (math.factorial(n) * m**n * multiplication))
        if (math.fabs(probs[n][-1] - probs[n][-2]) < eps): break



    sum = 0
    for i in range(1, len(probs[n])):
        sum += probs[n][i]
        print(' + (', n, ':', i, ') ', probs[n][i])
    print(sum)


# Сохраняем мат. ожидания числа занятых операторов.
MBusyOps = [0] * OPS
for n in range(1, OPS):
    for i in range(0, n + 1):
        MBusyOps[n] += i * probs[n][i]
    for i in range(n + 1, len(probs[n])):
        MBusyOps[n] += n * probs[n][i]


# Функция вывода мат. ожидания числа занятых операторов.
def drawMBusyOps():
    x = [i for i in range(1, OPS)]
    y = [MBusyOps[i] for i in x]
    graph.title("Мат. ожидание числа занятых операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
drawMBusyOps()
graph.show()
