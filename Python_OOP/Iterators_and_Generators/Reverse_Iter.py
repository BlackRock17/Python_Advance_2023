class reverse_iter:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.idx) > len(self.numbers):
            raise StopIteration
        idx = self.idx
        self.idx -= 1
        return self.numbers[idx]


reversed_list = reverse_iter([3, 4, 5, 6, 7])
for item in reversed_list:
    print(item)
