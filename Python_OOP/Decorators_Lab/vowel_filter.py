def vowel_filter(function):

    def wrapper():
        chars = function()
        return [char for char in chars if char.lower() in "aeoui"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "i"]

@vowel_filter
def test():
    return ["b", "r", "e", "q", "I"]


print(get_letters())
print(test())

