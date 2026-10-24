import numpy as np
def newton_method(f,df,x0,tol,max_iter):
    x = x0
    i = 0
    x_new = x - f(x)/df(x)
    error = abs(x_new-x)
    approx = np.array([])
    func_values = np.array([])
    step_size = np.array([])
    while error > tol and i < max_iter:
        if df(x) ==0:
            print("Newton method doesn't exists")
            return None
        x_new = x - f(x)/df(x)
        approx = np.append(approx,x_new)
        func_values = np.append(func_values,abs(f(x_new)))
        step_size = np.append(step_size,abs(x_new-x))
        error = abs(x_new-x)
        x = x_new
        i += 1
        print(i,x)
    return x 

def f(x):
    return 6*x**3 +3
def df(x):
    return 18*x**2 

root = newton_method(f,df,1,1e-6,150)
print(root)

        