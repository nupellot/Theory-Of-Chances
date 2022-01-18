import matplotlib.pyplot as graph
import math

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 23]

a = R[1]
c = G[1]
m = 100
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

for i in range(0, len(X)):
    print(i, '->', X[i])
print('Период:', len(X) - 1 - firstAppearance)
