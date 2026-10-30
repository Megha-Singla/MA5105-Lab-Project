#Bisection_Method
import numpy as np
import import_ipynb

from diagnostics import validate_bisection_inputs, check_stop

def bisection(f, a:float, b:float, tol:float, max_itr:int=200):
    """
    Args:
        f: any continuous function,
        a,b: initial guess,
        tol: small positive float value
        max_itr: maximum number of iterations

    Return:
        Approximate root of the continuous function f.
    """


    validate_bisection_inputs(f, a, b, tol, max_itr)


    #check end points are root or not
    if abs(f(a))<=tol:
         return a
    if abs(f(b))<=tol:
         return b
    else:
        #i initiates loop and also records iteration history
        i=0
        mid_pts=[]
        func_values=[]
        step_size=[]
        while i <max_itr :
            c=(a+b)/2
            fc=f(c)
            #mid_pts records all approximations.
            mid_pts.append(c)

            #All residual errors
            func_values.append(abs(f(c)))


            step_size.append(abs((a-b)/2))



            status, message = check_stop(fc, step_size[-1], i, tol, max_itr)
            if status != "continue":
                return f'mid_pt:{c}, iter:{i}, {status}, {message}, mid_pts: {mid_pts}, func_values:{func_values}, step_size:{step_size}' 
            i+=1                    
            if abs(f(c)) <= tol:
                break      

            if f(a)*f(c)<0:
                b=c
            else:
                a=c

def f(x):
     return 6*x**3+3


print(bisection(f, -4,7,1e-6, 150))

