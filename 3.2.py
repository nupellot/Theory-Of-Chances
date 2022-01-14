import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 27, 28, 22]

amountOfMachines = G[1] + B[1] + R[2] + B[2] + R[3] + G[3]  # Количество станков.
servicePeriod = RGB[1] + RGB[1] + RGB[2]  # Среднее время между наладками.
breakPeriod = RGB[1] + RGB[2] + RGB[3]  # Среднее время наладки.

# Интенсивности потоков.
l = 1 / breakPeriod  # Лямбда. [з/с]
mu = 1 / servicePeriod  # Мю. [з/с]
p = l / mu  # Загрузка системы.


probs = [[] for i in range(0, amountOfMachines)]  # Все возможные вероятности.
for n in range(1, amountOfMachines):  # Варьируем число наладчиков (n).
    m = amountOfMachines - n  # m - число мест в очереди.
    denominator = 0
    for i in range(0, n + 1):
        denominator += (math.factorial(n + m) * l**i) / (math.factorial(i) * math.factorial(n + m - i) * mu**i)
    for i in range(1, m + 1):
        denominator += (math.factorial(n + m) * l**(n + i)) / (math.factorial(n) * math.factorial(m - i) * n**i * mu**(n + i))

    p0 = 1 / denominator
    probs[n].append(p0)
    for i in range(1, n + 1):
        probs[n].append((math.factorial(n + m) * l**i * p0) / (math.factorial(i) * math.factorial(n + m - i) * mu**i))
    for i in range(n + 1, n + m + 1):
        probs[n].append((math.factorial(n + m) * l**i * p0) / (math.factorial(n) * math.factorial(n + m - i) * n**(i - n) * mu**i))

for n in range(1, amountOfMachines):
    summ = 0;
    for i in range(0, amountOfMachines):
        summ += probs[n][i]
        print(' + (', n, ':', i, ') ', probs[n][i])
    print(summ)



# Сохраняем мат. ожидания числа простаивающих станков.
MIdleMachines = [0] * amountOfMachines
for n in range(1, amountOfMachines):
    for i in range(0, amountOfMachines + 1):
        MIdleMachines[n] += probs[n][i] * i

# Сохраняем мат. ожидания числа станков ожидающих обслуживания.
MWaitMachines = [0] * amountOfMachines
for n in range(1, amountOfMachines):
    for i in range(n + 1, amountOfMachines + 1):
        MWaitMachines[n] += probs[n][i] * (i - n)

# Сохраняем вероятности ожидания обслуживания.
PWait = [0] * amountOfMachines
for n in range(1, amountOfMachines):
    for i in range(n + 1, amountOfMachines + 1):
        PWait[n] += probs[n][i]

# Сохраняем мат. ожидания числа занятых наладчиков.
MBusyFixers = [0] * amountOfMachines
for n in range(1, amountOfMachines):
    for i in range(0, n + 1):
        MBusyFixers[n] += probs[n][i] * i
    for i in range(n + 1, amountOfMachines + 1):
        MBusyFixers[n] += probs[n][i] * n

# Сохраняем коэффициенты занятости наладчиков.
KBusyFixers = [0] * amountOfMachines
for n in range(1, amountOfMachines):
    for i in range(n + 1, amountOfMachines + 1):
        KBusyFixers[n] += MBusyFixers[n] / n



x = [i for i in range(1, amountOfMachines)]
y = [MIdleMachines[i] for i in x]
graph.title("Мат. ожидание числа простаивающих станков")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("M")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()

y = [MWaitMachines[i] for i in x]
graph.title("Мат. ожидание числа станков, ожидающих обслуживания.")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("M")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()

y = [PWait[i] for i in x]
graph.title("Вероятность ожидания обслуживания")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("P")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()

y = [MBusyFixers[i] for i in x]
graph.title("Мат. ожидание числа занятых наладчиков")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("P")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()

y = [KBusyFixers[i] for i in x]
graph.title("Коэффициент занятости наладчиков")  # Название графика.
graph.xlabel("n")  # Подпись оси абсцисс.
graph.ylabel("k")  # Подпись оси ординат.
graph.bar(x, y)
graph.show()
