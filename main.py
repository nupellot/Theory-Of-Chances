import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 27, 28, 22]

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.

# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]
p = l / m  # Загрузка системы.

# Расчитываем все вероятности состояний
probs = [[[0] for i in range(0, 13)] for j in range(0, 13)]
# print(*probs, sep='\n')
for n in range(1, 13):  # n = Число операторов.
	# chanceOfRefuse.append([])
	for m in range(0, 13):  # m = Число мест в очереди.
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
		# chanceOfRefuse[n][m] = probs[n][m][-1]
		# print('n: ', n, ' m: ', m, ': ', probs[n][m][-1])


# Сохраняем вероятности отказа.
chanceOfRefuse = [[0]*13 for i in range(0,13)]
for n in range(1, 13):
	for m in range(0, 13):
		chanceOfRefuse[n][m] = probs[n][m][-1]

# Сохраняем мат. ожидания числа занятых операторов.
MBusyOps = [[0]*13 for i in range(0,13)]
for n in range(1, 13):
	for m in range(0, 13):
		for i in range(0, n + m + 1):
			# print('n: ', n, ' m: ', m)
			# print('len(probs[n][m]): ', len(probs[n][m]), ' i: ', i)
			if (i <=n): MBusyOps[n][m] += probs[n][m][i] * i
			if (i > n): MBusyOps[n][m] += probs[n][m][i] * n

# Сохраняем вероятности существования очереди.
chanceOfQueue = [[0]*13 for i in range(0,13)]
for n in range(1, 13):
	for m in range(0, 13):
		for i in range(0, n + m + 1):
			if (i > n): chanceOfQueue[n][m] += probs[n][m][i]

# Сохраняем мат. ожидания длины очереди.
MQueueLength = [[0]*13 for i in range(0,13)]
for n in range(1, 13):
	for m in range(0, 13):
		for i in range(0, n + m + 1):
			if (i > n): MQueueLength[n][m] += probs[n][m][i] * m


# Функция вывода вероятности отказа.
def drawChanceOfRefuse(n):
    x = [i for i in range(0, 13)]
    y = [chanceOfRefuse[n][i] for i in x]
    graph.title("Вероятность отказа")  # Название графика.
    graph.xlabel("m")  # Подпись оси абсцисс.
    graph.ylabel("P")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
for i in range(1, 13):
    drawChanceOfRefuse(i)
graph.show()

# Функция вывода мат. ожидания кол-ва занятых операторов.
def drawMBusyOps(n):
    x = [i for i in range(0, 13)]
    y = [MBusyOps[n][i] for i in x]
    graph.title("Мат. Ожидание числа занятых операторов")  # Название графика.
    graph.xlabel("m")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
for i in range(1, 13):
    drawMBusyOps(i)
graph.show()

# Функция вывода вероятности существования очереди.
def drawChanceOfQueue(n):
    x = [i for i in range(0, 13)]
    y = [chanceOfQueue[n][i] for i in x]
    graph.title("Вероятность существования очереди")  # Название графика.
    graph.xlabel("m")  # Подпись оси абсцисс.
    graph.ylabel("P")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
for i in range(1, 13):
    drawChanceOfQueue(i)
graph.show()

# Функция мат. ожидания длины очереди.
def drawMQueueLength(n):
    x = [i for i in range(0, 13)]
    y = [MQueueLength[n][i] for i in x]
    graph.title("Мат. Ожидание длины очереди")  # Название графика.
    graph.xlabel("m")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
for i in range(1, 13):
    drawMQueueLength(i)
graph.show()
