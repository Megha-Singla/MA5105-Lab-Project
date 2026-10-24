import numpy as np
def newton_method(f,df,x0,tol,max_iter):
    x = x0
    i = 0
    x_new = x - f(x)/df(x)
    error = abs(x_new-x)
    while error > tol and i < max_iter:
        if df(x) ==0:
            print("Newton method doesn't exists")
            return None
        x_new = x - f(x)/df(x)
        error = abs(x_new-x)
        x = x_new
        i += 1
        print(i,x)
    return x 

def f(x):
    return x**2 -2
def df(x):
    return 2*x

root = newton_method(f,df,1,1e-6,50)
print(root)

        