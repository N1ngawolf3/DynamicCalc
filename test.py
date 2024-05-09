import numpy as np

R = 0.038 #mm
lR = 0.2
am = 0.05
Sh = 0.076 #mm
x0 = Sh*am #mm
k = 1.05
p1 = 1.92*(10**5) #Pa
p2 = 10.211*(10**5) #Pa
D = 0.1
def rad(phi):
    return phi*np.pi/180

def x(phi):
    return R*(1 - np.cos(rad(phi)) + lR/4 * (1 - np.cos(2*rad(phi))))


def plot(phi):
    if 0 <= phi <= 48.337:
        y = [p2/((x(phi)+x0)/x0)**k]
    elif 48.337 < phi <= 180:
        y = [p1]
    elif 180 < phi <= 316.092:
        y = [p1 / ((x(phi) + x0) / (x0+Sh)) ** k]
    elif 316.092 < phi <= 360:
        y = [p2]
    return y

print(plot(315))