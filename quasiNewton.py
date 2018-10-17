# -*- coding: utf-8 -*-
from __future__ import division
import numpy 
from sympy import *
#拟牛顿法
THRESHOLD = 1e-8

u,v=symbols('u v')
a,b=symbols('a b')
#x,y,z,t=symbols('x y z t')
#z = a - b + 2*a ** 2+ 2*a*b + b**2
z = 2*a ** 2 + b**2 - 4*a + 2 

H_1 = eye(2)

form = z.diff(a)
form_1 = z.diff(b)
hession_11 = form.diff(a)
hession_12 = form.diff(b)
hession_21 = form_1.diff(a)
hession_22 = form_1.diff(b)

ma = numpy.asarray([[hession_11, hession_12], [hession_21, hession_22]], dtype= numpy.float)
X_0, Y_0 = (2, 1)
#哈希矩阵
ma_hess = Matrix(ma)
#哈希矩阵的逆矩阵
ma_inv = ma_hess.inv()

count = 0
g_0 = Matrix([0,0])
inti_X_Y = Matrix([X_0, Y_0])

diff_a_val = form.subs({a:X_0,b:Y_0})
diff_b_val = form_1.subs({a:X_0,b:Y_0})
g_1 = Matrix([diff_a_val, diff_b_val])

while True:
    
    if (numpy.abs(g_1[0]) + numpy.abs(g_1[1])) > THRESHOLD:
        delta_g = g_1 - g_0
        
        d = - H_1 * g_1
        
        inter_X_Y =  inti_X_Y + u * d
        zz = z.subs({a:inter_X_Y[0],b:inter_X_Y[1]}).diff(u)
        gamma = solve(zz, u)[0]
        #print gamma, ' gamma'
        final_X_Y = inter_X_Y.subs({u : gamma})
        
        delta_X_Y = final_X_Y - inti_X_Y
        
        diff_a_val = form.subs({a:final_X_Y[0],b:final_X_Y[1]})
        diff_b_val = form_1.subs({a:final_X_Y[0],b:final_X_Y[1]})
        g_2 = Matrix([diff_a_val, diff_b_val])
        delta_g = g_2 - g_1
        inter_H = H_1 + (delta_X_Y * delta_X_Y.transpose()) / (delta_g.transpose() * delta_X_Y)[0] -(H_1 * delta_g * delta_g.transpose() *H_1) / (delta_g.transpose() *H_1 * delta_g)[0]
        H_1 = inter_H
        inti_X_Y = final_X_Y
        g_0 = g_1
        g_1 = g_2
        count = count + 1
        print '----------the ', count, 'th iteration-------------'
    else:
        print  ' Final location is ', final_X_Y, ' and the minimum is ', z.subs({a:final_X_Y[0], b:final_X_Y[1]})
        break
    