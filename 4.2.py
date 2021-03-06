import matplotlib.pyplot as graph
import math
import data

k1 = [
0.810,
0.811,
0.812,
0.813,
0.814,
0.815,
0.816,
0.817,
0.818,
0.819,
0.820,
0.821,
0.822,
0.823,
0.824,
0.825,
0.826,
0.827,
0.828,
0.829,
0.830,
0.831,
0.832,
0.833,
0.834,
0.835,
0.836,
0.837,
0.838,
0.839,
0.840,
0.841,
0.842,
0.843,
0.844,
0.845,
0.846,
0.847,
0.848,
0.849,
0.850,
0.851,
0.852,
0.853,
0.854,
0.855,
0.856,
0.857,
0.858,
0.859,
0.860,
0.861,
0.862,
0.863,
0.864,
0.865,
0.866,
0.867,
0.868,
0.869,
0.870,
0.871,
0.872,
0.873,
0.874,
0.875,
0.876,
0.877,
0.878,
0.879,
0.880,
0.881,
0.882,
0.883,
0.884,
0.885,
0.886,
0.887,
0.888,
0.889,
0.890,
0.891,
0.892,
0.893,
0.894,
0.895,
0.896,
0.897,
0.898,
0.899,
0.900,
0.901,
0.902,
0.903,
0.904,
0.905,
0.906,
0.907,
0.908,
0.797,
]

k2 = [
0.559,
0.579,
0.560,
0.551,
0.538,
0.585,
0.501,
0.564,
0.532,
0.540,
0.634,
0.601,
0.538,
0.550,
0.571,
0.580,
0.579,
0.582,
0.550,
0.536,
0.502,
0.605,
0.591,
0.586,
0.596,
0.579,
0.582,
0.544,
0.497,
0.553,
0.581,
0.549,
0.477,
0.633,
0.579,
0.573,
0.579,
0.559,
0.564,
0.534,
0.550,
0.554,
0.567,
0.520,
0.585,
0.618,
0.511,
0.565,
0.601,
0.554,
0.524,
0.615,
0.561,
0.526,
0.549,
0.577,
0.561,
0.555,
0.574,
0.579,
0.565,
0.575,
0.559,
0.576,
0.536,
0.580,
0.543,
0.589,
0.604,
0.517,
0.554,
0.556,
0.546,
0.578,
0.556,
0.644,
0.602,
0.560,
0.588,
0.553,
0.560,
0.555,
0.579,
0.585,
0.578,
0.551,
0.547,
0.539,
0.586,
0.544,
0.576,
0.563,
0.495,
0.588,
0.600,
0.567,
0.563,
0.641,
0.594,
0.564,
]

M1 = [
0.199,
0.267,
0.198,
0.148,
0.204,
0.245,
0.162,
0.248,
0.233,
0.212,
0.332,
0.242,
0.187,
0.153,
0.188,
0.237,
0.255,
0.212,
0.178,
0.195,
0.128,
0.274,
0.217,
0.335,
0.251,
0.288,
0.187,
0.224,
0.149,
0.221,
0.234,
0.278,
0.141,
0.389,
0.212,
0.303,
0.153,
0.178,
0.211,
0.184,
0.223,
0.135,
0.233,
0.212,
0.359,
0.271,
0.136,
0.236,
0.255,
0.250,
0.182,
0.297,
0.158,
0.155,
0.257,
0.224,
0.234,
0.194,
0.180,
0.220,
0.167,
0.208,
0.228,
0.238,
0.176,
0.233,
0.223,
0.257,
0.297,
0.180,
0.172,
0.267,
0.206,
0.206,
0.201,
0.263,
0.230,
0.291,
0.296,
0.201,
0.185,
0.186,
0.182,
0.246,
0.169,
0.167,
0.164,
0.183,
0.279,
0.269,
0.247,
0.232,
0.145,
0.168,
0.252,
0.211,
0.210,
0.289,
0.237,
0.183,
]

M2 = [
0.053,
0.098,
0.069,
0.028,
0.051,
0.068,
0.051,
0.091,
0.063,
0.084,
0.167,
0.095,
0.073,
0.045,
0.061,
0.070,
0.092,
0.082,
0.069,
0.065,
0.030,
0.091,
0.043,
0.173,
0.077,
0.120,
0.049,
0.086,
0.030,
0.083,
0.072,
0.094,
0.039,
0.179,
0.056,
0.123,
0.037,
0.042,
0.066,
0.050,
0.056,
0.024,
0.081,
0.072,
0.194,
0.095,
0.045,
0.089,
0.080,
0.083,
0.037,
0.115,
0.046,
0.048,
0.119,
0.073,
0.082,
0.080,
0.045,
0.082,
0.037,
0.044,
0.066,
0.072,
0.039,
0.073,
0.082,
0.102,
0.108,
0.036,
0.037,
0.095,
0.067,
0.053,
0.058,
0.110,
0.078,
0.135,
0.122,
0.057,
0.069,
0.050,
0.058,
0.096,
0.032,
0.060,
0.036,
0.047,
0.075,
0.084,
0.102,
0.059,
0.035,
0.038,
0.068,
0.077,
0.066,
0.113,
0.071,
0.052,
]

R = [2, 8, 11, 9]
G = [1, 5, 8, 6]
B = [2, 7, 11, 8]
RGB = [5, 20, 30, 23]

n = [100, 10, 25, 50]


print('\n################# ???????????????????????????? ???????????????????? ?????????????? ##########################')
# ???????????????????????????? ???????????????????? ??????????????.
# ???????????? ?????????????????????? - ????????????????. ???????????? - n
Mk1 = [0] * 4  # ???????????????????? ??????????????.
Dk1 = [0] * 4  # ?????????????????? ???????????????????? ??????????????????.
Sk1 = [0] * 4  # ???????????????????????? ???????????????????? ??????????????????.

# ?????? k1
print('k1')
for i in range(0, len(n)):  # ?????? ?????????????? n.
    for j in range(0, n[i]):
        Mk1[i] += 1 / n[i] * k1[j]
    for j in range(0, n[i]):
        Dk1[i] += 1 / n[i] * (k1[j] - Mk1[i])**2
    for j in range(0, n[i]):
        Sk1[i] += 1 / (n[i] - 1) * (k1[j] - Mk1[i])**2
    print(n[i], '->', '[x]', '%.7f' % Mk1[i], '[D]', '%.7f' % Dk1[i], '[S^2]', '%.7f' % Sk1[i])

Mk2 = [0] * 4  # ???????????????????? ??????????????.
Dk2 = [0] * 4  # ?????????????????? ???????????????????? ??????????????????.
Sk2 = [0] * 4  # ???????????????????????? ???????????????????? ??????????????????.
# ?????? k2
print('k2')
for i in range(0, len(n)):  # ?????? ?????????????? n.
    for j in range(0, n[i]):
        Mk2[i] += 1 / n[i] * k2[j]
    for j in range(0, n[i]):
        Dk2[i] += 1 / n[i] * (k2[j] - Mk2[i])**2
    for j in range(0, n[i]):
        Sk2[i] += 1 / (n[i] - 1) * (k2[j] - Mk2[i])**2
    print(n[i], '->', '[x]', '%.7f' % Mk2[i], '[D]', '%.7f' % Dk2[i], '[S^2]', '%.7f' % Sk2[i])

MM1 = [0] * 4  # ???????????????????? ??????????????.
DM1 = [0] * 4  # ?????????????????? ???????????????????? ??????????????????.
SM1 = [0] * 4  # ???????????????????????? ???????????????????? ??????????????????.
# ?????? M1
print('M1')
for i in range(0, len(n)):  # ?????? ?????????????? n.
    for j in range(0, n[i]):
        MM1[i] += 1 / n[i] * M1[j]
    for j in range(0, n[i]):
        DM1[i] += 1 / n[i] * (M1[j] - MM1[i])**2
    for j in range(0, n[i]):
        SM1[i] += 1 / (n[i] - 1) * (M1[j] - MM1[i])**2
    print(n[i], '->', '[x]', '%.7f' % MM1[i], '[D]', '%.7f' % DM1[i], '[S2]', '%.7f' % SM1[i])

MM2 = [0] * 4  # ???????????????????? ??????????????.
DM2 = [0] * 4  # ?????????????????? ???????????????????? ??????????????????.
SM2 = [0] * 4  # ???????????????????????? ???????????????????? ??????????????????.
# ?????? M2
print('M2')
for i in range(0, len(n)):  # ?????? ?????????????? n.
    for j in range(0, n[i]):
        MM2[i] += 1 / n[i] * M2[j]
    for j in range(0, n[i]):
        DM2[i] += 1 / n[i] * (M2[j] - MM2[i])**2
    for j in range(0, n[i]):
        SM2[i] += 1 / (n[i] - 1) * (M2[j] - MM2[i])**2
    print(n[i], '->', '[x]', '%.7f' % MM2[i], '[D]', '%.7f' % DM2[i], '[S^2]', '%.7f' % SM2[i])


def covcor(x, y, n, mx, my, sx, sy):
    summ = 0
    for i in range(0, n):
        summ += (x[i] - mx) * (y[i] - my)
    cov = summ / (n - 1)
    cor = cov / math.sqrt(sx) / math.sqrt(sy)
    print(n, '->', '%.7f' % cov, '%.7f' % cor)

print('\n################## ???????????????????? ?? ???????????????????? ???????????????????? ?????????????? ###################')
print('       ????????????????????  ????????????????????')
print('k1 & k2')
for i in range(0, len(n)):
    covcor(k1, k2, n[i], Mk1[i], Mk2[i], Sk1[i], Sk2[i])
print('k1 & M1')
for i in range(0, len(n)):
    covcor(k1, M1, n[i], Mk1[i], MM1[i], Sk1[i], SM1[i])
print('k1 & M2')
for i in range(0, len(n)):
    covcor(k1, M2, n[i], Mk1[i], MM2[i], Sk1[i], SM2[i])
print('k2 & M1')
for i in range(0, len(n)):
    covcor(k2, M1, n[i], Mk2[i], MM1[i], Sk2[i], SM1[i])
print('k2 & M2')
for i in range(0, len(n)):
    covcor(k2, M2, n[i], Mk2[i], MM2[i], Sk2[i], SM2[i])
print('M1 & M2')
for i in range(0, len(n)):
    covcor(M1, M2, n[i], MM1[i], MM2[i], SM1[i], SM2[i])


print('\n#################### ?????????????????????????? ?????????????????? ???????????????????? ?????????????? ##################')
n = [10, 25, 60]
t = [[1.83, 3.25], [1.71, 2.80], [1.68, 2.70]]
def interval(nn, a, mx, sx):
    left = mx - sx/math.sqrt(n[nn]) * t[nn][a]
    right = mx + sx/math.sqrt(n[nn]) * t[nn][a]
    if (a == 0): a = 0.1
    if (a == 1): a = 0.01
    print('?????? n =', n[nn], '& a =', a, '?????????????????????????? ????????????????:', '%.7f' % left, '< M <', '%.7f' % right)

print('k1')
for i in range(0, len(n)):
    interval(i, 0, Mk1[0], Sk1[0])
    interval(i, 1, Mk1[0], Sk1[0])
print('k2')
for i in range(0, len(n)):
    interval(i, 0, Mk2[0], Sk2[0])
    interval(i, 1, Mk2[0], Sk2[0])
print('M1')
for i in range(0, len(n)):
    interval(i, 0, MM1[0], SM1[0])
    interval(i, 1, MM1[0], SM1[0])
print('M2')
for i in range(0, len(n)):
    interval(i, 0, MM2[0], SM2[0])
    interval(i, 1, MM2[0], SM2[0])


# ???????? ????????????.
# for i in range(len(k1Intervals) - 1, int(len(k1Intervals)/2), - 1):
#     # print('Checked')
#     if (k1Intervals[i][1] < 5):
#         k1Intervals[i - 1][1] += k1Intervals[i][1]
#         k1Intervals.pop(i)
#         # print('Removed')

# #???????? ??????????.
# for j in range(2):
#     print()
#     for i in range(0, int(len(k1Intervals) / 2)):
#         print(i, 'Checked')
#         if (k1Intervals[i][1] < 5):
#             k1Intervals[i + 1][1] += k1Intervals[i][1]
#             k1Intervals[i + 1][0] = k1Intervals[i][0]
#             k1Intervals.remove(k1Intervals[i])
#             print(i, 'Removed')






k1Intervals = [[0]*2 for i in range(0, 70)]
intLength = 1 / len(k1Intervals)
# ?????????????? ?????????? ?????????????? ????????????????????.
for i in range(0, len(k1Intervals)):
    k1Intervals[i][0] = 0 + i * intLength
# ?????????????????????? ?????? ???????????????? ???????????????????? ???? ????????????????????.
for i in range(0, len(k1)):
    k1Intervals[int(k1[i] // intLength)][1] += 1

for i in range(0, len(k1Intervals)):
    if k1Intervals[i][1] < 5:
        k1Intervals[i][1] = 0

summ = 0
for i in range(len(k1Intervals)):
    print(i, k1Intervals[i][0], k1Intervals[i][1])
    summ += k1Intervals[i][1]
print(summ)



k2Intervals = [[0]*2 for i in range(0, 50)]
intLength = 1 / len(k2Intervals)
# ?????????????? ?????????? ?????????????? ????????????????????.
for i in range(0, len(k2Intervals)):
    k2Intervals[i][0] = 0 + i * intLength
# ?????????????????????? ?????? ???????????????? ???????????????????? ???? ????????????????????.
for i in range(0, len(k2)):
    k2Intervals[int(k2[i] // intLength)][1] += 1

for i in range(0, len(k2Intervals)):
    if k2Intervals[i][1] < 5:
        k2Intervals[i][1] = 0


M1Intervals = [[0]*2 for i in range(0, 50)]
intLength = 1 / len(M1Intervals)
# ?????????????? ?????????? ?????????????? ????????????????????.
for i in range(0, len(M1Intervals)):
    M1Intervals[i][0] = 0 + i * intLength
# ?????????????????????? ?????? ???????????????? ???????????????????? ???? ????????????????????.
for i in range(0, len(M1)):
    M1Intervals[int(M1[i] // intLength)][1] += 1

for i in range(0, len(M1Intervals)):
    if M1Intervals[i][1] < 5:
        M1Intervals[i][1] = 0

summ = 0
for i in range(len(M1Intervals)):
    print(i, M1Intervals[i][0], M1Intervals[i][1])
    summ += M1Intervals[i][1]
print(summ)



# ?????????? ?????????????? ????????????????????.
x = [k1Intervals[i][0] for i in range(50, len(k1Intervals))]
# ???????????? ????????????????????.
intNumber = [i for i in range(50, len(k1Intervals))]
# ???????????????????? ???????????????? ?? ????????????????????.
y = [k1Intervals[i][1] for i in intNumber]
graph.title("?????????????????????????? k1")  # ???????????????? ??????????????.
graph.xlabel("?????????????? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.bar(x, y, edgecolor="white", color = 'red', align = 'edge', width = 1 / len(k1Intervals))
graph.show()

# ?????????? ?????????????? ????????????????????.
x = [k2Intervals[i][0] for i in range(0, len(k2Intervals) - 20)]
# ???????????? ????????????????????.
intNumber = [i for i in range(0, len(k2Intervals) - 20)]
# ???????????????????? ???????????????? ?? ????????????????????.
y = [k2Intervals[i][1] for i in intNumber]
graph.title("?????????????????????????? k2")  # ???????????????? ??????????????.
graph.xlabel("?????????????? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.bar(x, y, edgecolor="white", color = 'red', align = 'edge', width = 1 / len(k2Intervals))
graph.show()

# ?????????? ?????????????? ????????????????????.
x = [M1Intervals[i][0] for i in range(0, len(M1Intervals) - 30)]
# ???????????? ????????????????????.
intNumber = [i for i in range(0, len(M1Intervals) - 30)]
# ???????????????????? ???????????????? ?? ????????????????????.
y = [M1Intervals[i][1] for i in intNumber]
graph.title("?????????????????????????? M1")  # ???????????????? ??????????????.
graph.xlabel("?????????????? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.bar(x, y, edgecolor="white", color = 'red', align = 'edge', width = 1 / len(M1Intervals))
graph.show()







graph.title("?????????????????????????? ???????????????? k1")  # ???????????????? ??????????????.
graph.xlabel("k1")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.hist(k1, bins = 11)
# graph.show()

graph.title("?????????????????????????? ???????????????? k2")  # ???????????????? ??????????????.
graph.xlabel("k2")  # ?????????????? ?????? ??????????????.
graph.hist(k2, bins = 11)
# graph.show()

graph.title("?????????????????????????? ???????????????? M1")  # ???????????????? ??????????????.
graph.xlabel("M1")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.hist(M1, bins = 6)
# graph.show()

graph.title("?????????????????????????? ???????????????? M2")  # ???????????????? ??????????????.
graph.xlabel("M2")  # ?????????????? ?????? ??????????????.
graph.ylabel("??????-???? ???????????????? ?? ??????????????????")  # ?????????????? ?????? ??????????????.
graph.grid()
graph.hist(M2, bins = 4)
# graph.show()
