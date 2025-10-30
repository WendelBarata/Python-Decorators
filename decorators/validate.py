# ############# ALL YOU NEED IS THE FOLLOWING FUNCTION ########################

"""Useful information about the decorator:
- The validate decorator validates function arguments against custom conditions
- Useful for input validation, data sanitization, and enforcing constraints
- Can validate ranges, types, patterns, and custom conditions
- Raises ValueError with descriptive messages on validation failure
"""

from functools import wraps
from typing import Callable, Any


def validate(**validators: Callable[[Any], bool]) -> callable:
    """
    Decorator that validates function arguments using custom validators

    This decorator checks arguments against validation functions before
    executing the decorated function. Each validator should return True
    if the argument is valid, False otherwise.

    Parameters:
        validators (dict): keyword arguments mapping parameter names to
                          validation functions

    Returns:
        callable: decorated function with argument validation

    Example:
        @validate(age=lambda x: x >= 0, name=lambda x: len(x) > 0)
        def create_user(name, age):
            return f"User {name}, age {age}"
    """
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameter names
            import inspect
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())

            # Map positional arguments to parameter names
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Validate each argument
            for param_name, validator in validators.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]

                    # Run the validator
                    try:
                        is_valid = validator(value)
                    except Exception as e:
                        raise ValueError(
                            f"Error validating '{param_name}': {e}"
                        )

                    if not is_valid:
                        raise ValueError(
                            f"Validation failed for '{param_name}' "
                            f"with value: {value}"
                        )

            return func(*args, **kwargs)

        return wrapper
    return decorator


###############################################################################
# Here's a generic example of how to use the decorator ########################
###############################################################################


# First: define validation functions for your parameters
# Second: use @validate with parameter_name=validation_function pairs

# General structure of the function that you want to decorate with validate
@validate(n=lambda x: x > 0)  # Validate that n is positive
def YourFunction(n):  # This function will have validated arguments
    ...  # Your code here
    return n  # Return the result of the function if needed


###############################################################################
# Sample function to test the validate decorator ##############################
###############################################################################


@validate(
    age=lambda x: 0 <= x <= 150,
    name=lambda x: len(x) > 0 and len(x) < 50
)
def create_user(name: str, age: int) -> str:
    """Create a user with validated inputs"""
    return f"Created user: {name}, age {age}"


@validate(
    price=lambda x: x > 0,
    quantity=lambda x: x > 0 and x == int(x)
)
def calculate_total(price: float, quantity: int) -> float:
    """Calculate total cost with validation"""
    return price * quantity


@validate(
    email=lambda x: '@' in x and '.' in x,
    password=lambda x: len(x) >= 8
)
def register(email: str, password: str) -> str:
    """Register user with validated credentials"""
    return f"Registered: {email}"


@validate(
    score=lambda x: 0 <= x <= 100,
    grade=lambda x: x in ['A', 'B', 'C', 'D', 'F']
)
def record_grade(student: str, score: int, grade: str) -> str:
    """Record student grade with validation"""
    return f"{student}: {score} ({grade})"


# Test the decorator
print(create_user("John Doe", 30))  # Valid
print(calculate_total(10.5, 3))  # Valid
print(register("user@example.com", "securepass123"))  # Valid
print(record_grade("Alice", 95, "A"))  # Valid

# Uncomment to test validation failures:
# print(create_user("", 30))  # Fails: empty name
# print(calculate_total(-10, 3))  # Fails: negative price
# print(register("invalid-email", "pass"))  # Fails: invalid email and short password
# print(record_grade("Bob", 150, "A"))  # Fails: score out of range
