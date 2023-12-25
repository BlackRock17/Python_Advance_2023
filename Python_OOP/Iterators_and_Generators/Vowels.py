class vowels:
    All_VOWELS = "AYOEIUayoeiu"

    def __init__(self, str):
        self.str = str
        self.text = [el for el in self.str if el in vowels.All_VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.text:
            raise StopIteration

        return self.text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)



