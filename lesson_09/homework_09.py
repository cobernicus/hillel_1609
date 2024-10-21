def calculating_function(num1, num2):
    return num1 + num2


def reverse_string(some_string):
    # return string in reverse order
    result = some_string[::-1]
    return result


def get_unique_elements(some_string):
    # Use set to check whether all elements are unique
    unique_el = set(some_string)
    if len(unique_el) > 10:
        return True
    else:
        return False


def get_only_string(lst1):
    lst2 = []
    # Iterate over each element
    for i in lst1:
        # Element type check
        if isinstance(i, str):
            lst2.append(i)
    return lst2


def word_with_specific_letter(word):
    while True:
        # Check whether the specified letter is in the word
        if 'h' in word or 'H' in word:
            break
        else:
            return "This word does not contain the letter 'h' or 'H'. Try again."