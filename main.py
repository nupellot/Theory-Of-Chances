import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 27, 28, 22]

OPS = 13  # Вычисленное в прошлом пункте число операторов. Выступает верхней границей в данном пункте.

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.

# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]
p = l / m  # Загрузка системы.
print(p)

# Расчитываем все вероятности состояний.
Pns = [0] * OPS


lowBound = 1
n = 1
while p / n >= 1:
	lowBound += 1
	n += 1

for n in range(lowBound, OPS):  # Варьируем число операторов.
	if (p / n <= 1):  # В иных случаях очередь будет бесконечно возрастать.
		denominator = 0
		# Занимаем операторов.
		for i in range(0, n + 1):
			denominator += p**i / math.factorial(i)
		# Занимаем места в очереди.
		a = p / n
		if (a < 1):
			denominator += p**n / math.factorial(n) * (a) / (1 - a)
		Pns[n] = 1 / denominator

# Сохраняем мат. ожидания числа занятых операторов.
MBusyOps = [0] * OPS
for n in range(lowBound, OPS):
	if (p / n <= 1):  # В иных случаях очередь будет бесконечно возрастать.
		MBusyOps[n] = p

# Сохраняем коэффициенты загрузки операторов.
KBusyOps = [0] * OPS
for n in range(1, OPS):
	KBusyOps[n] = MBusyOps[n] / n

# Сохраняем вероятности существования очереди.
queueExists = [0] * OPS
for n in range(lowBound, OPS):
	a = p / n
	print(p)
	print(n)
	queueExists[n] = Pns[n] * a / (1 - a)

# Сохраняем мат. ожидания длины очереди.
MQueueLength = [0] * OPS
for n in range(lowBound, OPS):
	a = p / n
	MQueueLength[n] = a * Pns[n] / (1 - a)**2




# Функция вывода мат. ожидания числа занятых операторов.
def drawMBusyOps():
    x = [i for i in range(lowBound, OPS)]
    y = [MBusyOps[i] for i in x]
    graph.title("Мат. ожидание числа занятых операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
drawMBusyOps()
graph.show()

# Функция вывода коэффициентов загрузки операторов.
def drawKBusyOps():
    x = [i for i in range(lowBound, OPS)]
    y = [KBusyOps[i] for i in x]
    graph.title("Коэффициент загрузки операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("K")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
drawKBusyOps()
graph.show()

# Функция вывода вероятности существования очереди.
def drawQueueExists():
    x = [i for i in range(lowBound, OPS)]
    y = [queueExists[i] for i in x]
    graph.title("Вероятность существования очереди")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("P")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
drawQueueExists()
graph.show()

# Функция вывода мат. ожидания длины очереди.
def drawMQueueLength():
    x = [i for i in range(lowBound, OPS)]
    y = [MQueueLength[i] for i in x]
    graph.title("Мат. ожидание длины очереди")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label=f"n = {n}")
    graph.legend()
drawMQueueLength()
graph.show()
