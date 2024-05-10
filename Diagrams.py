import matplotlib.pyplot as plt
import numpy as np
from config import *
from math import asin

fig = plt.figure()
forces = fig.add_subplot(1, 1, 1)
# tang_forces = fig.add_subplot(2, 1, 2)


def x(phi):
    return R*(1 - np.cos(phi) + lR/4 * (1 - np.cos(2*phi)))

def beta(phi):
    return asin(lR * np.sin(phi))

# initializing the data

x_axis = np.arange(0, 2*np.pi, 0.01)
y = []
yj = []
yfr = []
ysum = []
ypow = []
ysh = []
#Gas forces
for angle in x_axis:
    if angle > 2*np.pi:
        angle -= 2*np.pi
    if 0 <= angle <= phi1:
        y += [(p2 / ((x(angle) + x0) / x0) ** k - pev)*(np.pi*D**2/4)]
    elif phi1 < angle <= np.pi:
        y += [(p1 - pev)*(np.pi*D**2/4)]
    elif np.pi < angle <= phi2:
        y += [(p1 / ((x(angle) + x0) / (x0+Sh)) ** k - pev)*(np.pi*D**2/4)]
    elif phi2 < angle <= 2*np.pi:
        y += [(p2 - pev)*(np.pi*D**2/4)]

for angle in x_axis:
    yj += [-(2*np.pi*n/60)**2*R*(np.cos(angle)+lR*np.cos(2*angle))*mps]

for angle in x_axis:
    if 0 <= angle <= np.pi:
        yfr += [-2/3*Nfr/(Cm*z)]
    elif np.pi < angle <= 2*np.pi:
        yfr += [2/3*Nfr/(Cm*z)]

for i in range(len(y)):
    ysum += [yfr[i]+y[i]+yj[i]]

for i in range(len(y)):
    current_ysum = yfr[i]+y[i]+yj[i]
    ypow += [current_ysum * np.tan(beta(x_axis[i]))]

for i in range(len(y)):
    current_ysum = yfr[i] + y[i] + yj[i]
    ysh += [current_ysum/np.cos(beta(x_axis[i]))]

T = []
for i in range(len(y)):
    T += [ysh[i]*np.sin(x_axis[i]+beta(x_axis[i]))]

Tav = [-5911 for _ in range(len(x_axis))]


def Tang(phi):
    return ysh*np.sin(x_axis[i]+beta(x_axis[i]))


# Tsum = []
# for i in range(len(x_axis)):
#     phism = 2*np.pi/z
#     Tsum += [ysh[i]*np.sin(x_axis[i]+beta(x_axis[i])) + ysh[i]*np.sin(x_axis[i]+beta(x_axis[i]))]

forces.grid(True)
forces.set_title('Диаграмма Сил')
forces.plot(x_axis, y)
forces.plot(x_axis, yj, linestyle=':')
forces.plot(x_axis, yfr, linestyle='-')
forces.plot(x_axis, ysum, linestyle='--')
forces.plot(x_axis, ypow, ls='-.')
# forces.plot(x_axis, ysh)


# plt.xlim(0, 2*np.pi+0.006)
# plt.ylim(-2900, 6700)
# plt.yticks(np.arange(-3000, 7000, 500))
# plt.xticks(np.arange(0, 2*np.pi+0.006, np.pi/4))

# x_axis.set_xticklabels(labels)
plt.legend(['Газовые силы', "Силы Инерции", "Силы трения",
             'Суммарная сила', "Мощность"]
            )

labels = ['$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$',
          r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']

forces.set_xlabel(r'$\phi$, рад')
forces.set_ylabel('Силы, Н\n'
              'Мощность, Вт')
forces.set_xlim(0, 2*np.pi+0.006)
forces.set_ylim(-3000, 7000)
forces.set_xlim(0, 2*np.pi+0.006)
forces.set_yticks(np.arange(-3000, 7000, 500))
forces.set_xticks(np.arange(0, 2*np.pi+0.006, np.pi/4))
forces.set_xticklabels(labels)
# tang_forces.set_xlabel(r'$\phi$, рад')
# tang_forces.set_xlim(0, 2*np.pi+0.006)
# tang_forces.set_xticks(np.arange(0, 2*np.pi+0.006, np.pi/4))
# tang_forces.set_xticklabels(labels)

plt.grid(True)
plt.show()
