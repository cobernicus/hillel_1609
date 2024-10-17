def sum_numbers_in_string(s):
    try:
        parts = s.split(',')
        total = sum(int(part) for part in parts)
        return total
    except ValueError:
        return "Can't do it!"

strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
results = [sum_numbers_in_string(s) for s in strings]

for result in results:
    print(result)
