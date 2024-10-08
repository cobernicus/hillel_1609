text = input('Enter your text:')
print(text)

list1=[]
for char in text:
    list1.append(char)

unique_characters = (len(set(text)))
print('Unique characters:', unique_characters)

check = unique_characters > 10
print('More than 10 unique characters:', check)
