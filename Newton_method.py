import numpy as np
import import_ipynb
from diagnostics import validate_newton_inputs, check_derivative, check_stop 
def newton_method(f,df,x0,tol,max_iter):
    validate_newton_inputs(f,df,x0,tol,max_iter)
    x = x0
    i = 0
    x_new = x - f(x)/df(x)
    error = abs(x_new-x)
    approx = np.array([])
    func_values = np.array([])
    step_size = np.array([])
    while error > tol and i < max_iter:
        check_derivative(df(x),x)
        x_new = x - f(x)/df(x)
        #print(x_new)
        approx = np.append(approx,x_new)
        func_values = np.append(func_values,abs(f(x_new)))
        step_size = np.append(step_size,abs(x_new-x))
        #print(approx)
        error = abs(x_new-x)
        x = x_new
        fx = f(x)
        status, message = check_stop(fx,step_size[-1],i,tol,max_iter)
        if status!= "continue":
            return f'value:{x},iteration:{i},status:{status},message:{message},approx:{approx},func_values:{func_values},step_size:{step_size}'    
        i += 1
        #print(approx,func_values,step_size)


def f(x):
    return 6*x**3 +3
def df(x):
    return 18*x**2 

root = newton_method(f,df,1,1e-6,150)
print(root)

        