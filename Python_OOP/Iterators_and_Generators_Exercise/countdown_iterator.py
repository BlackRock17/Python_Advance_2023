class countdown_iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):

        if self.count < 0:
            raise StopIteration

        num = self.count
        self.count -= 1
        return num


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")



