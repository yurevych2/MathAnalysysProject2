from math import sin, cos, e

def single_derivative(func: str) -> str:
    """
    Computes derivative of a single function.
    Some examples:
    >>> single_derivative("sin(5x)")
    '5*cos(5x)'
    >>> single_derivative("cos(3x)")
    '-3*sin(3x)'
    >>> single_derivative("e^(-2x)")
    '-2*e^(-2x)'
    >>> single_derivative("x^(3)")
    '3*x^(2)'
    >>> single_derivative("121")
    '0'
    """
    pass


def combine_multipliers(der, others):
    """
    :param der: already found derivative of a single function
    :param others: other functions-multipliers
    :return: result of single chain rule
    >>> found_derivative = "2"
    >>> other = ["x^(2)", "sin(1x)"]
    >>> combine_multipliers(found_derivative, other)
    '2*x^(2)*sin(1x)'
    >>> found_derivative = "2"
    >>> other = []
    >>> combine_multipliers(found_derivative, other)
    '2'
    """
    pass


def derivative_of_product(some_func: list) -> str:
    """
    Using the chain rule finds a derivative of a product
    example of input: ["-1", "e^(5x)", "cos(-2x)"]
    approximate output: 5*e^(5x)*-1*cos(-2x) + 2*sin(-2x)*-1*e^(5x)
    :param some_func: list of functions.
    """
    res = []
    # chain rule
    for ind, func in enumerate(some_func):
        others = some_func[:ind] + some_func[ind + 1:]
        der = single_derivative(func)
        adder = combine_multipliers(der, others)
        res.append(adder)
    return " + ".join(res)


def find_derivative(equation: str) -> str:
    """
    Main function. Receives the sum of functions as a string
    :param equation: str representation of the function.

    Examples: '2*cos(1x)*x^(1) + x^(1)*e^(2x)', or '2*x^(3) + -5*sin(-3x)'
    There will not be no inputs like '-sin(1x)', or '-e^(3x)', or '-x^(2)'.
    Instead the minus will be converted to '-1':  '-1*sin(1x)' ...

    :return: returns the derivative of the sum of functions.
    """
    parts = equation.split(" + ")

    separately_computed = []
    for part in parts:
        multipliers = part.split("*")
        separately_computed.append(derivative_of_product(multipliers))

    return " + ".join(separately_computed)


def evaluate_at_point(function: str, point: float) -> float:
    """
    Evaluates a function at a certain point.
    :param function: same requirements as in the previous task.
    :param point: some value of x
    :return: value of the function when x == point

    >>> evaluate_at_point("x*sin(x) + -2*e^(x)", '2') == 2*sin(2) + -2*e**(2)
    """
    function = function.replace('^', '**')
    func_to_eval = ''
    for index, element in enumerate(function):
        if element == 'x':
            if function[index-1].isnumeric():
                func_to_eval = func_to_eval + '*x'
            if function[index+1].isnumeric():
                func_to_eval = func_to_eval + 'x*'
            if not (function[index-1].isnumeric() and function[index+1].isnumeric()):
                func_to_eval = func_to_eval + 'x'
        else:
            func_to_eval += element
    
    return eval(func_to_eval.replace('x', point))


def newtons_method(func: str, a: float, b: float, start: float, epsilon: float) -> float:
    """
    Finds the solution of the equation (x value) 'func = 0' on the interval [a, b].
    Start with 'start' and stops  when |func(x_i)| < epsilon

    Example of input: newtons_method(func="x^(2) + -4", a=1, b=3, start=1.5, epsilon=0.000001).
    Should return approximately 2.

    :param func: a string representation of a function
    :param a: start of the interval
    :param b: end of the interval
    :param start: x_0
    :param epsilon: accuracy of the final point
    :return: point at x-axis
    >>> newtons_method('x**2 - 2*x', a=-2, b=3, start=-1, epsilon=1)
    -1
    """
    if b<=a:
        return 'Incorrect segment [a; b], b<=a'
    x0 = start
    while (abs(evaluate_at_point(func, x0)) - epsilon > 0) or (b-x0 < epsilon):
        try:
            x0 -= evaluate_at_point(func,x0) / evaluate_at_point(find_derivative(func,x0))
        except ZeroDivisionError:
            return 'F(x0) = 0. Division by zero'
    
    return x0
