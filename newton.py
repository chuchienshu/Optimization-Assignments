# -*- coding: utf-8 -*-
import numpy 
from sympy import *
#阻尼牛顿法
THRESHOLD = 1e-6

u,v=symbols('u v')
a,b=symbols('a b')
z = a - b + 2*a ** 2+ 2*a*b + b**2

form = z.diff(a)
form_1 = z.diff(b)
hession_11 = form.diff(a)
hession_12 = form.diff(b)
hession_21 = form_1.diff(a)
hession_22 = form_1.diff(b)

#print hession_11,' ',hession_12,' ',hession_21,' ',hession_22
ma = numpy.asarray([[hession_11, hession_12], [hession_21, hession_22]])
X_0, Y_0 = (0, 0)
#哈希矩阵
ma_hess = Matrix(ma)
#哈希矩阵的逆矩阵
ma_inv = ma_hess.inv()

count = 0

while True:
    
    diff_a_val = form.subs({a:X_0,b:Y_0})
    diff_b_val = form_1.subs({a:X_0,b:Y_0})
    
    if (numpy.abs(diff_a_val) + numpy.abs(diff_b_val)) > THRESHOLD:
        m_1 = Matrix([diff_a_val, diff_b_val])
        #newton 方向
        d = - ma_inv * m_1
        
        tup = u * d + Matrix([X_0, Y_0])
        z_diff = z.subs({a:tup[0],b:tup[1]}).diff(u)
        
        gamma = solve(z_diff, u)[0]
        
        outcome = tup.subs({u:gamma} )
        count = count + 1
        print '----------the ', count, 'th iteration-------------'
        X_0 , Y_0= outcome[0], outcome[1]
    else:
        print  ' Final location is ', outcome, ' and the minimum is ', z.subs({a:outcome[0], b:outcome[1]})
        break
    