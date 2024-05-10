from matplotlib.animation import FuncAnimation
import numpy as np
from math import asin
import matplotlib.pyplot as plt
from config import *


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi+0.006, 0.01)
y = np.arange(0, 2*np.pi, 0.01)

inertia_diagram, = ax.plot(x, y)
gas_force_diagram, = ax.plot(x, y)
friction_force_diagram, = ax.plot(x, y)
sum_force_diagram, = ax.plot(x, y)
pow_diagram, = ax.plot(x, y)
phase = np.arange(0, 2*np.pi, 0.01)


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


def inertia_force(angles):
    y = []
    for angle in angles:
        if angle > 2*np.pi:
            angle -= 2*np.pi
        y += [-(2*np.pi*n/60)**2*R *
              (np.cos(angle)+lR*np.cos(2*angle))*mps]
    return y


def friction_force(angles):
    y = []
    for angle in angles:
        if angle > 2*np.pi:
            angle -= 2*np.pi
        if 0 <= angle <= np.pi:
            y += [-2 / 3 * Nfr / (Cm * z)]
        elif np.pi < angle <= 2 * np.pi:
            y += [2 / 3 * Nfr / (Cm * z)]
    return y


def sum_force(angles):
    y = []
    yg = gas_force(angles)
    yi = inertia_force(angles)
    yfr = friction_force(angles)
    for i in range(len(x)):
        y += [yg[i] + yi[i] + yfr[i]]
    return y


def pow(angles):
    y = []
    i = 0
    for el in sum_force(angles):
        y += [el*np.tan(asin(lR*np.sin(angles[i])))]
        i += 1
    return y


def update_forces(frame, inertia_diagram,
                  gas_force_diagram,
                  friction_force_diagram,
                  sum_force_diagram,
                  pow_diagram, x):
    # frame - параметр, который меняется от кадра к кадру
    # в данном случае - это начальная фаза (угол)
    # line - ссылка на объект gas_force_diagramD
    inertia_diagram.set_ydata(inertia_force(x + frame))
    gas_force_diagram.set_ydata(gas_force(x+frame))
    friction_force_diagram.set_ydata(friction_force(x+frame))
    sum_force_diagram.set_ydata(sum_force(x+frame))
    pow_diagram.set_ydata(pow(x+frame))
    return (inertia_diagram,
            gas_force_diagram,
            friction_force_diagram,
            sum_force_diagram,
            pow_diagram)



animation = FuncAnimation(
    fig,                # фигура, где отображается анимация
    func=update_forces,    # функция обновления текущего кадра
    frames=phase,       # параметр, меняющийся от кадра к кадру
    fargs=(inertia_diagram,
           gas_force_diagram,
           friction_force_diagram,
           sum_force_diagram,
           pow_diagram, x),    # дополнительные параметры для функции update_cos
    interval=5,       # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)       # зацикливать ли анимацию


plt.xlim(0, 2*np.pi)
plt.ylim(-2900, 6700)
plt.yticks(np.arange(-3000, 7000, 500))
plt.xticks(np.arange(0, 2*np.pi+0.006, np.pi/4))
ax.set_xlabel(r'$\phi$, рад')
ax.set_ylabel('Силы, Н\n'
              'Мощность, Вт')
labels = ['$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$',
          r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']
ax.set_xticklabels(labels)
ax.set_title('Диаграмма Сил')
plt.legend(['Силы Инерции', "Газовые силы", "Силы трения",
            'Суммарная сила', "Мощность"])
plt.grid(True)
plt.show()
