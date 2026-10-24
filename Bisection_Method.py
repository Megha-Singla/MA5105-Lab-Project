#Bisection_Method
import numpy as np
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

    #check end points are root or not
    if abs(f(a))<=tol:
         return a
    if abs(f(b))<=tol:
         return b
         


    #Check whether the interval has a sign change
    if f(a)*f(b)>0:
            return "Invalid interval"
            
    else:
        #i initiates loop and also records iteration history
        i=0
        mid_pts=np.array([])
        func_values=np.array([])
        step_size=np.array([])
        while i <max_itr :
            c=(a+b)/2

            #mid_pts records all approximations.
            mid_pts=np.append(mid_pts,c)

            #All residual errors
            func_values=np.append(func_values, abs(f(c)))


            step_size=np.append(step_size, abs((a-b)/2))

            i+=1                    
            if abs(f(c)) <= tol:
                break      

            if f(a)*f(c)<0:
                b=c
            else:
                a=c
         
            
        # max_itr reached (failure to converge within the iteration limit)
        if abs(f(c))>tol:
             print("Maximum iteration reached before convergence")

    return c,i



def f(x):
     return 6*x**3+3


print(bisection(f, -4,7,1e-6, 150))

