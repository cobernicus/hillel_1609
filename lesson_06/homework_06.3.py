lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for element in lst1:
    if isinstance(element, str):
        lst2.append(element)

print(lst2)
