def is_palindrome(pal):
    pal = pal.lower()
    pal = pal.strip()
    return pal[::-1] == pal
