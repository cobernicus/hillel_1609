import random

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(3, 9))
print('List with random numbers:', rand_list)

even_list = [num for num in rand_list if num % 2 == 0]
print('Even numbers from the list:', even_list)

sum_even_list = sum(even_list)
print('Sum of numbers from the list:', sum_even_list)
