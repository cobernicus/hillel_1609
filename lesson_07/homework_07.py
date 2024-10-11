# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print('Sum:', result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print('Average:', int(average))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

original_string = input('Enter your text:')
reversed_string = reverse_string(original_string)
print('Original:', original_string)
print('Reversed:', reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def more_10_uchars(text):
    unique_characters = len(set(text))
    return unique_characters > 10

# Function usage:
text = 'Some string for check my function'
result = more_10_uchars(text)
print('More than 10 unique characters:', result)

# task 8
def contains_H(text):
    return 'H' in text or 'h' in text

# Function usage:
text = "Some string for check my function"
result = contains_H(text)
print('Contains H or h:', result)

# task 9
def count_capitalized_words(text):
    words = text.split()
    capitalized_words_count = sum(1 for word in words if word.istitle())
    return capitalized_words_count

# Function usage:
text = "Some string for Check my Function"
result = count_capitalized_words(text)
print('Number of capitalized words:', result)

# task 10
def remainder(a, b):
    return a % b

# Function usage:
a = 10
b = 3
result = remainder(a, b)
print('Remainder of', a, 'divided by', b, 'is:', result)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""