import numpy as np
import import_ipynb
from diagnostics1 import validate_newton_inputs, check_derivative, check_stop
def newton_method(f,df,x0,tol,max_iter):
    conv = False
    x = x0
    i = 0
    x_new = x - f(x)/df(x)
    error = abs(x_new-x)
    approx = np.array([])
    func_values = np.array([])
    step_size = np.array([])
    while error > tol and i < max_iter:
        if abs(df(x)) < tol: # need to check the derivative near to zero
            print("The derivative is closing to zero or is zero") # Needs to be checked for zero or non-zero
            return x, approx, func_values, step_size      #storing the partial data
        
        x_new = x - f(x)/df(x)
        #print(x_new)
        approx = np.append(approx,x_new)
        func_values = np.append(func_values,abs(f(x_new)))
        step_size = np.append(step_size,abs(x_new-x))
        #print(approx)
        error = abs(x_new-x)
        x = x_new
        i += 1
        print(i,x)
        #print(approx,func_values,step_size)
    if error <= tol:     # Iteration has reached the point to converge and it tells it converges.
        conv = True
        print("Converged")
    else:
        print("Maximum iteration has reached before convergence")
    return x, approx, func_values,step_size
def f(x):
    return 6*x**3 +3
def df(x):
    return 18*x**2 

root = newton_method(f,df,1,1e-6,150)
print(root)

        