class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

# Example of usage:
my_list = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(my_list)

for item in reverse_iter:
    print(item)



class EvenNumberIterator:
    def __init__(self, N):
        self.N = N
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.N:
            raise StopIteration
        return self.current

# Example of usage:
N = 10
even_iter = EvenNumberIterator(N)

for number in even_iter:
    print(number)
