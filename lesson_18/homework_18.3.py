import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Example usage
@log_arguments_and_result
def add(a, b):
    return a + b

# Function call
add(5, 3)


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception occurred in {func.__name__}: {e}")
    return wrapper

# Example usage
@handle_exceptions
def divide(a, b):
    return a / b

# Function call
divide(10, 0)
