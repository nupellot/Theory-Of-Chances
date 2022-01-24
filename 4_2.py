import matplotlib.pyplot as plt
from math import floor, sqrt

x = [[0.784, 0.818, 0.783, 0.804, 0.774, 0.819, 0.754, 0.800, 0.772, 0.746, 0.804, 0.813, 0.766, 0.768, 0.784, 0.790,
      0.799, 0.788, 0.782, 0.763, 0.741, 0.796, 0.804, 0.797, 0.787, 0.780, 0.767, 0.779, 0.741, 0.762, 0.791, 0.805,
      0.750, 0.809, 0.787, 0.781, 0.781, 0.773, 0.790, 0.762, 0.780, 0.761, 0.789, 0.749, 0.804, 0.824, 0.758, 0.779,
      0.806, 0.810, 0.763, 0.808, 0.803, 0.723, 0.763, 0.795, 0.772, 0.742, 0.753, 0.792, 0.777, 0.806, 0.772, 0.793,
      0.766, 0.804, 0.748, 0.809, 0.822, 0.763, 0.759, 0.787, 0.764, 0.778, 0.775, 0.791, 0.814, 0.763, 0.789, 0.797,
      0.743, 0.776, 0.786, 0.780, 0.762, 0.786, 0.771, 0.759, 0.772, 0.794, 0.780, 0.803, 0.765, 0.772, 0.796, 0.783,
      0.786, 0.822, 0.787, 0.777],
     [0.571, 0.542, 0.554, 0.549, 0.525, 0.570, 0.527, 0.600, 0.547, 0.560, 0.627, 0.615, 0.516, 0.525, 0.565, 0.583,
      0.581, 0.566, 0.581, 0.555, 0.508, 0.610, 0.575, 0.610, 0.615, 0.569, 0.569, 0.535, 0.480, 0.550, 0.584, 0.584,
      0.488, 0.665, 0.559, 0.583, 0.579, 0.546, 0.573, 0.525, 0.552, 0.547, 0.580, 0.514, 0.585, 0.621, 0.523, 0.583,
      0.608, 0.572, 0.520, 0.625, 0.565, 0.528, 0.574, 0.585, 0.551, 0.575, 0.551, 0.574, 0.553, 0.584, 0.565, 0.598,
      0.556, 0.572, 0.542, 0.580, 0.619, 0.505, 0.584, 0.579, 0.567, 0.575, 0.574, 0.606, 0.581, 0.525, 0.592, 0.582,
      0.567, 0.577, 0.567, 0.580, 0.569, 0.547, 0.542, 0.519, 0.577, 0.547, 0.524, 0.556, 0.483, 0.595, 0.599, 0.586,
      0.552, 0.630, 0.611, 0.559],
     [0.186, 0.213, 0.173, 0.195, 0.187, 0.237, 0.185, 0.255, 0.195, 0.219, 0.364, 0.273, 0.157, 0.145, 0.188, 0.216,
      0.218, 0.201, 0.217, 0.178, 0.139, 0.321, 0.256, 0.313, 0.203, 0.195, 0.144, 0.192, 0.086, 0.205, 0.202, 0.301,
      0.150, 0.344, 0.188, 0.295, 0.176, 0.129, 0.206, 0.170, 0.183, 0.136, 0.260, 0.170, 0.375, 0.225, 0.125, 0.260,
      0.236, 0.239, 0.148, 0.253, 0.170, 0.118, 0.260, 0.238, 0.197, 0.187, 0.176, 0.226, 0.160, 0.205, 0.179, 0.218,
      0.178, 0.229, 0.185, 0.203, 0.250, 0.130, 0.162, 0.244, 0.232, 0.204, 0.228, 0.178, 0.210, 0.147, 0.247, 0.226,
      0.146, 0.196, 0.162, 0.239, 0.165, 0.166, 0.161, 0.142, 0.178, 0.228, 0.149, 0.245, 0.167, 0.156, 0.233, 0.226,
      0.268, 0.275, 0.225, 0.183],
     [0.062, 0.107, 0.055, 0.049, 0.046, 0.079, 0.050, 0.098, 0.066, 0.107, 0.222, 0.131, 0.048, 0.039, 0.048, 0.075,
      0.082, 0.080, 0.079, 0.061, 0.039, 0.114, 0.103, 0.142, 0.090, 0.088, 0.049, 0.092, 0.019, 0.059, 0.072, 0.098,
      0.033, 0.158, 0.043, 0.116, 0.043, 0.031, 0.087, 0.041, 0.050, 0.018, 0.084, 0.057, 0.244, 0.085, 0.032, 0.130,
      0.089, 0.092, 0.032, 0.077, 0.030, 0.033, 0.113, 0.069, 0.049, 0.063, 0.060, 0.078, 0.036, 0.052, 0.044, 0.083,
      0.039, 0.102, 0.079, 0.084, 0.097, 0.031, 0.046, 0.111, 0.076, 0.065, 0.068, 0.080, 0.072, 0.028, 0.101, 0.070,
      0.058, 0.057, 0.046, 0.098, 0.062, 0.049, 0.044, 0.055, 0.055, 0.086, 0.024, 0.083, 0.046, 0.052, 0.051, 0.085,
      0.091, 0.131, 0.066, 0.049]]

xAvg, disp, dispRate = [[]]*4, [[]]*4, [[]]*4
n = [10, 25, 50, 100]
graph = [0.0002, 0.0005, 0.001, 0.0006]
name = ["Коэффициент загрузки кассира", "Средняя длина очереди"]
for k in range(4):
    print(name[floor(k/2)], ' ', 1 + k % 2, ':', sep='')
    print("  n", "xAvg", "sig^2", "  S^2", sep='\t\t')
    for i in n:
        xAvg[k].append(sum(x[k][:i]) / i)
        disp[k].append(sum([(j-xAvg[k][-1])**2 for j in x[k][:i]]) / i)
        dispRate[k].append(disp[k][-1] * i / (i-1))
        print("%3d\t %.5f\t%.7f\t%.7f" % (i, xAvg[k][-1], disp[k][-1], dispRate[k][-1]))
    print()
    # interval = dispRate[k][-1] / 2
    interval = graph[k]
    a = [interval * i for i in range(floor(1/interval))]
    y = [0]*len(a)
    for i in range(n[-1]):
        y[floor(x[k][i]//interval)] += 1
    while y[0] < 5:
        y[1] += y[0]
        y.pop(0)
        a.pop(0)
    while y[-1] < 5:
        y[-2] += y[-1]
        y.pop(-1)
        a.pop(-1)
    plt.bar(a, y, width=(floor((3-k)/3)+0.8)*interval, align="edge")
    # plt.show()


cov = [[0]*6 for i in range(0, 4)]
p = [[0]*6 for i in range(0, 4)]
nameShort = ['k', 'q']
for i in range(len(n)):
    print("\nn = ", n[i], ":\n\t\t\t  cov\t\t\t\t  p", sep='')
    for j in range(3):
        for k in range(j + 1, 4):
            cov[i][j] = (sum([ (x[j][z] - xAvg[j][i]) * (x[k][z]-xAvg[k][i]) for z in range(n[i])]) / (n[i]-1))
            p[i][j] = (cov[i][-1] / sqrt(dispRate[j][i] * dispRate[k][i]))
            print(nameShort[floor(j/2)], 1+j%2, ',', nameShort[floor(k/2)], 1+k%2, "\t%.7f\t%15.7f" % (cov[i][-1], p[i][-1]), sep='')

n = [10, 25, 60]
a = [0.1, 0.01]
t = [[1.83, 3.25], [1.71, 2.80], [1.67, 2.66]]
interv = [[[0]*2 for j in range(3)] for i in range(4)]

x_, S2 = [[]]*4, [[]]*4

for k in range(4):
    for i in n:
        x_[k].append(sum(x[k][:i]) / i)
        S2[k].append(sum([(j - x_[k][-1]) ** 2 for j in x[k][:i]]) / (i-1))

    print('\n', name[floor(k/2)], ' ', 1 + k % 2, ':', sep='')
    for i in range(3):
        print("\tn = ", n[i], ':', sep='')
        for j in range(2):
            interv[k][i][j] = S2[k][i] / sqrt(n[i]) * t[i][j]
            print("a =", a[j], "\t%.5f < M < %.5f" % (x_[k][i] - interv[k][i][j], x_[k][i] + interv[k][i][j]))
        print()