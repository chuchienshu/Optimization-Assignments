# -*- coding: utf-8 -*-
import numpy 
from sympy import *
#坐标轮换法
THRESHOLD = 1e-8

u=symbols('u')
a,b,c=symbols('a b c')
z = 3 * a**2 + 2*b**2 + c**2

e_1 = Matrix([1,0,0])
e_2 = Matrix([0,1,0])
e_3 = Matrix([0,0,1])

init_loc = Matrix([1,2,3])
count = 0

while True:
    inter_loc = init_loc + e_1 * u
    inter_out = z.subs({a:inter_loc[0], b: inter_loc[1], c: inter_loc[2]}).diff(u)
    e_1_out = solve(inter_out, u)
    inter_loc_1 = inter_loc.subs({u: e_1_out[0]})
    inter_loc_2 = inter_loc_1 + e_2 * u
    inter_out = z.subs({a:inter_loc_2[0], b: inter_loc_2[1], c: inter_loc_2[2]}).diff(u)
    e_2_out = solve(inter_out, u)
    inter_loc_3 = inter_loc_2.subs({u: e_2_out[0]})
    
    inter_loc_3 = inter_loc_3 + e_3 * u
    inter_out = z.subs({a:inter_loc_3[0], b: inter_loc_3[1], c: inter_loc_3[2]}).diff(u)
    e_3_out = solve(inter_out, u)
    inter_loc_4 = inter_loc_3.subs({u: e_3_out[0]})
    init_loc = inter_loc_4
    count = count + 1
    print '----------the ', count, 'th iteration-------------'
    if (numpy.sum(numpy.abs(inter_loc_4 - init_loc ))) < THRESHOLD:
        print  ' Final location is ', inter_loc_4, ' and the minimum is ', z.subs({a:inter_loc_4[0], b:inter_loc_4[1], c: inter_loc_4[2]})
        break
    