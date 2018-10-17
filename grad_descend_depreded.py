# -*- coding: utf-8 -*-
from autograd import elementwise_grad as egrad  # for functions that vectorize over inputs
import matplotlib.pyplot as plt
import autograd.numpy as np  # Thinly-wrapped numpy
from autograd import grad    # The only autograd function you may ever need
import numpy 
import sympy as sp
#最速下降法

THRESHOLD = 0.01
def func(x):                 # Define a function
    return  3*x * x + 16 * x - 9

grad_func = grad(func)       # Obtain its gradient function
x = -3.0
count = 0
while True:
    grad_val = grad_func(x)  
    print 'outcome is  ', func(x)
    print x, ' **x'
    print grad_val, type(grad_val)
    if numpy.abs(grad_val) > THRESHOLD:
        d = -grad_val
        b = sp.Symbol("b")
        _x = sp.Symbol("_x")
        #得到一阶导数形式
        form =  sp.diff(func(_x), _x)
        form = form.replace('_x', '%f - b * %f' % (x, grad_val))
        #form = sp.sympify(form)
        #gamma 值,sp.S()转换字符串为函数形式，用于求解
        gamma = sp.solve(form, b)[0]
        #print 'gamma ', gamma
        x = x + gamma * d
        x = float(x)
        count = count + 1
        print '----------the ', count, 'th iteration-------------'
    else:
        print  ' Final location is ', final_X_Y, ' and the minimum is ', z.subs({a:final_X_Y[0], b:final_X_Y[1]})
        break    
    
#linspacke 用于生成等差数列，第三个参数表示数列中数的个数
x = np.linspace(-7, 7, 200)
plt.plot(x, func(x))
plt.plot(x, egrad(func)(x))
'''x, egrad(tanh)(x),                                     # first  derivative
x, egrad(egrad(tanh))(x),                              # second derivative
x, egrad(egrad(egrad(tanh)))(x),                       # third  derivative
x, egrad(egrad(egrad(egrad(tanh))))(x),                # fourth derivative
x, egrad(egrad(egrad(egrad(egrad(tanh)))))(x),         # fifth  derivative
x, egrad(egrad(egrad(egrad(egrad(egrad(tanh))))))(x))'''  
plt.show()