import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import Animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

R = 0.038
lR = 0.2
am = 0.05
Sh = 0.076
x0 = Sh*am
k = 1.05
pev = 1.99*10**5
D = 0.1

def rad(phi):
    return phi*np.pi/180


def x(phi):
    return R*(1 - np.cos(rad(phi)) + lR/4 * (1 - np.cos(2*rad(phi))))


# initializing the data
p1 = 1.92*(10**5)
p2 = 10.211*(10**5)
x_axis = np.arange(0, 360, 0.01)
y = []

for phi in x_axis:
    if 0 <= phi <= 48.337:
        y += [(p2 / ((x(phi) + x0) / x0) ** k - pev)*(np.pi*D**2/4)]
    elif 48.337 < phi <= 180:
        y += [(p1 - pev)*(np.pi*D**2/4)]
    elif 180 < phi <= 316.092:
        y += [(p1 / ((x(phi) + x0) / (x0+Sh)) ** k- pev)*(np.pi*D**2/4)]
    elif 316.092 < phi <= 360:
        y += [(p2 - pev)*(np.pi*D**2/4)]


ax.grid(True)
ax.set_title("Pressure")
ax.plot(x_axis, y, '--')
plt.xlim(0, 360)


plt.show()
