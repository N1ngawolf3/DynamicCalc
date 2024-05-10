import numpy as np
from config import *
from sympy import symbols, Eq, solve



x = symbols('x')
equation = Eq((p2/((R*(1 - x + lR/4 * (1 - x))+x0)/x0)**k), p1)
solution = solve(equation, x)
print(solution[0])