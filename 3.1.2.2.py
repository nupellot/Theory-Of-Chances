import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 23]

OPS = 13  # Вычисленное в прошлом пункте число операторов. Выступает верхней границей в данном пункте.

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.

# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]
p = l / m  # Загрузка системы.

# Расчитываем все вероятности состояний.
probs = [[[0] for i in range(0, OPS)] for j in range(0, OPS)]
for n in range(1, OPS):  # n = Число операторов.
	for m in range(0, OPS):  # m = Число мест в очереди.
		denominator = 0
		# Проходим по всем операторам.
		for i in range(0, n + 1):
			denominator += 1 * p**i / math.factorial(i)
		# Проходим по всем местам в очереди.
		for i in range(1, m + 1):
			denominator += 1 * p**(n + i) / math.factorial(n) / n**i
		p0 = 1 / denominator

		# Считаем вероятности различных состояний системы.
		probs[n][m][0] = p0
		# print('p0 = ', p0)
		for i in range(1, n + 1):
			probs[n][m].append(p0 * p**i / math.factorial(i))
		for i in range(n + 1, n + m + 1):
			probs[n][m].append(p0 * p**i / math.factorial(n) / n**(i - n))


# Сохраняем вероятности отказа.
chanceOfRefuse = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(0, OPS):
		chanceOfRefuse[n][m] = probs[n][m][-1]

# Сохраняем мат. ожидания числа занятых операторов.
MBusyOps = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(0, OPS):
		for i in range(0, n + m + 1):
			if (i <=n): MBusyOps[n][m] += probs[n][m][i] * i
			if (i > n): MBusyOps[n][m] += probs[n][m][i] * n

# Сохраняем коэффициенты загрузки операторов.
KBusyOps = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(0, OPS):
		for i in range(0, n + m + 1):
			KBusyOps[n][m] = MBusyOps[n][m] / n

# Сохраняем вероятности существования очереди.
chanceOfQueue = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(0, OPS):
		for i in range(0, n + m + 1):
			if (i > n): chanceOfQueue[n][m] += probs[n][m][i]

# Сохраняем мат. ожидания длины очереди.
MQueueLength = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(0, OPS):
		for i in range(0, n + m + 1):
			if (i > n): MQueueLength[n][m] += probs[n][m][i] * m

# Сохраняем коэффициенты занятости мест в очереди.
KQueueBusy = [[0]*OPS for i in range(0,OPS)]
for n in range(1, OPS):
	for m in range(1, OPS):
		for i in range(0, n + m + 1):
			KQueueBusy[n][m] = MQueueLength[n][m] / m





# Функция вывода вероятности отказа.
def drawChanceOfRefuse(m):
    x = [i for i in range(1, OPS)]
    y = [chanceOfRefuse[i][m] for i in x]
    graph.title("Вероятность отказа")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("P")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawChanceOfRefuse(i)
graph.show()

# Функция вывода мат. ожидания числа занятых операторов.
def drawMBusyOps(m):
    x = [i for i in range(1, OPS)]
    y = [MBusyOps[i][m] for i in x]
    graph.title("Мат. Ожидание числа занятых операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawMBusyOps(i)
graph.show()

# Функция вывода коэффициента загрузки операторов.
def drawKBusyOps(m):
    x = [i for i in range(1, OPS)]
    y = [KBusyOps[i][m] for i in x]
    graph.title("Коэффициент загрузки операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("K")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawKBusyOps(i)
graph.show()

# Функция вывода вероятности существования очереди.
def drawChanceOfQueue(m):
    x = [i for i in range(1, OPS)]
    y = [chanceOfQueue[i][m] for i in x]
    graph.title("Вероятность существования очереди")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("P")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawChanceOfQueue(i)
graph.show()

# Функция вывода мат. ожидания длины очереди.
def drawMQueueLength(m):
    x = [i for i in range(1, OPS)]
    y = [MQueueLength[i][m] for i in x]
    graph.title("Мат. Ожидание длины очереди")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawMQueueLength(i)
graph.show()

# Функция коэффициента занятости мест в очереди.
def drawKQueueBusy(m):
    x = [i for i in range(1, OPS)]
    y = [KQueueBusy[i][m] for i in x]
    graph.title("Коэффициент занятости мест в очереди")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"m = {m}")
    graph.legend()
for i in range(1, OPS):
    drawKQueueBusy(i)
graph.show()
