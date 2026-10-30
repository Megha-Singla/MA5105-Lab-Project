
def validate_bisection_inputs(f, a, b, tol, max_iter):
    """Raise ValueError if the bisection inputs are invalid."""
    if tol <= 0:
        raise ValueError(f"tol must be positive, got {tol}.")
    if max_iter < 1:
        raise ValueError(f"max_iter must be at least 1, got {max_iter}.")
    if a >= b:
        raise ValueError(f"Need a < b, got a={a}, b={b}.")
    if f(a) * f(b) > 0:
        raise ValueError(f"No sign change on [{a}, {b}]: f(a) and f(b) have the "
                         "same sign. Choose a different interval.")


def validate_newton_inputs(f, df, x0, tol, max_iter):
    """Raise ValueError if the Newton inputs are invalid."""
    if not callable(f) or not callable(df):
        raise ValueError("f and df must both be functions.")
    if tol <= 0:
        raise ValueError(f"tol must be positive, got {tol}.")
    if max_iter < 1:
        raise ValueError(f"max_iter must be at least 1, got {max_iter}.")


def check_derivative(dfx, x, eps=1e-12):
    """Raise ZeroDivisionError if f'(x) is too close to zero for a Newton step."""
    if abs(dfx) < eps:
        raise ZeroDivisionError(f"f'(x) is almost zero (|f'(x)| = {abs(dfx):.2e}) "
                                f"at x = {x:.6g}. Try a different initial guess.")


def check_stop(fx, step, iteration, tol, max_iter):
    """
    Decide whether to stop. Returns (status, message):
      status = "converged"  -> stop, success
      status = "max_iter"   -> stop, failure
      status = "continue"   -> keep iterating
    The message reports the residual |f(x)|.
    """
    residual = abs(fx)
    if residual <= tol:
        return "converged", f"Converged: residual |f(x)| = {residual:.2e} <= tol = {tol}."
    if step <= tol:
        return "converged", f"Converged: step size {step:.2e} <= tol = {tol}."
    if iteration >= max_iter:
        return "max_iter", (f"Failed to converge in {max_iter} iterations "
                            f"(residual |f(x)| = {residual:.2e}).")
    return "continue", ""