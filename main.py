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


# Расчитываем все вероятности состояний.
probs = [[0]*OPS for i in range(0, OPS)]
for n in range(1, OPS):  # Варьируем число операторов.
	denominator = 0;
	# Занимаем операторов.
	for i in range(0, n + 1):
		denominator += p**i / math.factorial(i)
	# Занимаем места в очереди.
	a = p / n
	if (a < 1):
		denominator += p**n / math.factorial(n) * (a) / (1 - a)

# Сохраняем мат. ожидания числа занятых операторов.
MBusyOps = [0] * OPS
for n in range(1, OPS):
	MBusyOps[n] = p




# Функция вывода мат. ожидания числа занятых операторов.
def drawMBusyOps():
    x = [i for i in range(1, OPS)]
    y = [MBusyOps[i] for i in x]
    graph.title("Мат. ожидание числа занятых операторов")  # Название графика.
    graph.xlabel("n")  # Подпись оси абсцисс.
    graph.ylabel("M")  # Подпись оси ординат.
    graph.grid()  # Включение отображения сетки.
    graph.plot(x, y, label="n = {n}")
    graph.legend()
drawMBusyOps()
graph.show()






