import matplotlib.pyplot as graph
import math as math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 22]

callPeriod = R[1]  # Среднее время между звонками клиентов.
servicePeriod = G[1] + B[1] + RGB[2]  # Среднее время обслуживания.

# Интенсивности потоков.
l = 1 / callPeriod  # Лямбда. [з/с]
m = 1 / servicePeriod  # Мю. [з/с]


POfRefuse = []
MBusyOps = []
KBusyOps = [1]
for amountOfOperators in range(0, 50):
		denominator = 0
		for i in range(0, amountOfOperators + 1):
				denominator += 1 * (l/m)**i/math.factorial(i)
		p0 = 1 / denominator

		p = [p0]
		for i in range(1, amountOfOperators + 1):
			p.append(p0 * (l/m)**i / math.factorial(i))
		POfRefuse.append(p[-1])

		M = 0;
		for i in range(0, amountOfOperators + 1):
			M += i * p[i]
		MBusyOps.append(M)
		if (amountOfOperators >= 1):
			KBusyOps.append(M / amountOfOperators)

n = 0
while POfRefuse[n] > 0.01:
    n += 1
print(n)


x = [i for i in range(0, n + 1)]
y = [POfRefuse[i] for i in x]
graph.title("Вероятность отказа от числа операторов")  # заголовок
graph.xlabel("n")  # ось абсцисс
graph.ylabel("P")  # ось ординат
graph.grid()  # включение отображение сетки
graph.bar(x, y)
graph.show()



y = [MBusyOps[i] for i in x]
graph.title("Мат. Ожидание числа занятых операторов")  # заголовок
graph.xlabel("n")  # ось абсцисс
graph.ylabel("M")  # ось ординат
graph.grid()  # включение отображение сетки
graph.bar(x, y)
graph.show()



y = [KBusyOps[i] for i in x]
graph.title("Коэффициент загрузки операторов от их числа")  # заголовок
graph.xlabel("n")  # ось абсцисс
graph.ylabel("K")  # ось ординат
graph.grid()  # включение отображение сетки
graph.bar(x, y)
graph.show()
