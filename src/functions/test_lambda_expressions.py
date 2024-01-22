"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.
"""


def test_lambda_expressions():
    """Lambda Expressions"""

    # This function returns the sum of its two arguments: lambda a, b: a+b
    # Like nested function definitions, lambda functions can reference variables from the
    # containing scope.

    def make_increment_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44
    
    def make_decrement_function(alpha):
        return lambda number: number - alpha
    
    decrement_function = make_decrement_function(114)

    assert decrement_function(0) == -114
    assert decrement_function(114) == 0

    # Another use of lambda is to pass a small function as an argument.
    pairs = [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
    # Sort pairs by text key.
    pairs.sort(key=lambda pair: pair[0])

    # assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
    assert pairs == [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
