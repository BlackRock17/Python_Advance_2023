def palindrome(text: str, idx: int):

    if text[abs(idx)] != text[idx - 1]:
        return f"{text} is not a palindrome"

    if len(text) // 2 == abs(idx):
        return f"{text} is a palindrome"

    return palindrome(text, idx - 1)

