from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from config import *
import sys

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
y = np.arange(0, 2*np.pi, 0.01)

line, = ax.plot(x, y)
phasa = np.arange(0, 2*np.pi, 0.01)


def dist(phi):
    return R*(1 - np.cos(phi) + lR/4 * (1 - np.cos(2*phi)))


def gas_force(angles):
    y = []
    for angle in angles:
        if angle > 2*np.pi:
            angle -= 2*np.pi
        if 0 <= angle <= phi1:
            y += [(p2 / ((dist(angle) + x0) / x0) ** k - pev)*(np.pi*D**2/4)]
        elif phi1 < angle <= np.pi:
            y += [(p1 - pev)*(np.pi*D**2/4)]
        elif np.pi < angle <= phi2:
            y += [(p1 / ((dist(angle) + x0) / (x0+Sh)) ** k - pev)*(np.pi*D**2/4)]
        elif phi2 < angle <= 2*np.pi:
            y += [(p2 - pev)*(np.pi*D**2/4)]
    return y


def update_gas_force(frame, line, x):
    # frame - параметр, который меняется от кадра к кадру
    # в данном случае - это начальная фаза (угол)
    # line - ссылка на объект Line2D
    line.set_ydata(gas_force(x+frame))
    return [line]


animation = FuncAnimation(
    fig,                # фигура, где отображается анимация
    func=update_gas_force,    # функция обновления текущего кадра
    frames=phasa,       # параметр, меняющийся от кадра к кадру
    fargs=(line, x),    # дополнительные параметры для функции update_cos
    interval=5,       # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)       # зацикливать ли анимацию

plt.xlim(0, 2*np.pi)
plt.ylim(-1000, 7000)
plt.grid(True)
plt.show()
