# -*- coding: utf-8 -*-
from autograd import elementwise_grad as egrad  # for functions that vectorize over inputs
import matplotlib.pyplot as plt
from autograd import grad    # The only autograd function you may ever need
import numpy as np
from sympy import *
#最速下降法

THRESHOLD = 1e-1

u,v=symbols('u v')
a,b=symbols('a b')
z = 2*a ** 2 + b**2

a_diff = z.diff(a)
b_diff = z.diff(b)

init_loc = Matrix([1, 1])

count = 0
while True:
    grad_a = a_diff.subs({a: init_loc[0],  b: init_loc[1]})
    grad_b = b_diff.subs({a: init_loc[0],  b: init_loc[1]})
    neg_grad = -Matrix([grad_a, grad_b])
    inter_loc = init_loc + u * neg_grad
    z_diff = z.subs({a: inter_loc[0], b: inter_loc[1]}).diff(u)
    gamma = solve(z_diff, u)[0]
    #print gamma
    inter_loc = inter_loc.subs({u : gamma})
    init_loc = inter_loc
    if np.sum(np.abs(inter_loc )) > THRESHOLD:
        count = count + 1
        print '----------the ', count, 'th iteration-------------'
    else:
        print  ' Final location is ', inter_loc, ' and the minimum is ', z.subs({a:inter_loc[0], b:inter_loc[1]})
        break  
    
#linspacke 用于生成等差数列，第三个参数表示数列中数的个数
'''x = np.linspace(-7, 7, 200)
plt.plot(x, func(x))
plt.plot(x, egrad(func)(x))
plt.show()'''