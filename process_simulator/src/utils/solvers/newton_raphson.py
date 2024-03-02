from typing import Callable
import numpy as np


def newton_raphson(func: Callable[[float], float],
                   initial_guess: float,
                   func_prime: None | Callable[[float], float] = None,
                   tol=1e-6,
                   max_iter=100):
    """
    Implementation of Newton-Raphson method for solving non-linear equations.

    Parameters:
        func: function
            The function for which roots are to be found.
        initial_guess: float
            Initial guess for the root.
        func_prime: function
            The first derivative of the function. An approximation is used if not given.
        tol: float, optional
            Tolerance for convergence. Default is 1e-6.
        max_iter: int, optional
            Maximum number of iterations. Default is 100.

    Returns:
        float
            Approximation of the root.
        int
            Number of iterations used.

    Raises:
        ValueError: If the derivative is zero at the initial guess.
    """
    x = initial_guess
    iterations = 0
    while True:
        # Calculate the function value and its derivative at x
        f_x = func(x)
        f_prime_x = derivative(
            func, x) if func_prime is None else func_prime(x)

        if f_prime_x == 0:
            raise ValueError("Derivative is zero at the initial guess.")

        # Newton-Raphson update
        x_next = x - f_x / f_prime_x

        # Check for convergence
        if np.abs(x_next - x) < tol or iterations >= max_iter:
            break

        x = x_next
        iterations += 1

    return x, iterations


def derivative(func, x, h=1e-6) -> float:
    """
    An approximation of the derivative.
    """
    return (func(x + h) - func(x)) / h
