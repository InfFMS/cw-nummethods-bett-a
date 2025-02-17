import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * 10**-5
R = 8.314

def kelvin(t):
    return t + 273.15

def pressure(v, t=-130):
    return (R * kelvin(t) / (v - b)) - (a / v**2)

v = np.linspace((b+(10)**-5), (10**-3), 1000)
'''
# 1 задание

t = (-140, -130, -120, -110, -100)

for i in t:
    plt.plot(v, pressure(v,i))
plt.title('-120 градусов - критическая температура')
plt.show()
'''

plt.plot(v, pressure(v))
#plt.plot(v, 3664186.998)
plt.show()

# 2 задание
def find_min(q, j, f, eps=10**-7):
    while j - q > 2*eps:
        mid1 = q + (j - q) / 3
        mid2 = j - (j - q) / 3
        if f(mid1) < f(mid2):
            j = mid2
        else:
            q = mid1
    return (j + q)/2

def find_max(q, j, f, eps=10**-7):
    while j - q > 2*eps:
        mid1 = q + (j - q) / 3
        mid2 = j - (j - q) / 3
        if f(mid1) > f(mid2):
            j = mid2
        else:
            q = mid1
    return (j + q)/2


minn = 7.192946159592504e-05
maxx = 0.0001362141276684001
#print(find_min(6.5*10**-5, 8.5*10**-5, pressure))   # 7.192946159592504e-05
#print(find_max(1*10**-4, 1.5*10**-4, pressure))    # 0.0001362141276684001


# 3 задание
def find_len(f):
    v_forbid = np.linspace(minn, maxx, 1000)
    sum = 0
    for i in range(len(v) - 1):
        x1 = v_forbid[i]
        y1 = f(x1)
        x2 = v_forbid[i + 1]
        y2 = f(x2)
        sum += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return sum

#print(find_len(pressure))   # 940301.6483963607

def find_solution(a, b, f, eps=10**-7):
    while b - a >= 2 * eps:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c

    return c

def equation(v):
    P = 3664186.998
    return pressure(v) - P

# 4 задание не закончено,
# 5 не начатое




