class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.idx >= len(self.dictionary):
            raise StopIteration

        index = self.idx
        self.idx += 1
        return self.dictionary[index]


result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
    print(x)
