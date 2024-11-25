# A generator that returns a sequence of even numbers from 0 to N.
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

# Example of usage:
n = 10
for number in even_numbers(n):
    print(number)

# A generator that generates the Fibonacci sequence up to a certain number N
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Example of usage:
n = 100
for number in fibonacci(n):
    print(number)
