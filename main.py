def is_palindorme(text: str) -> bool:
    is_palindorme: bool = True

    for i, _ in enumerate(text):
        if text[i-1] != text[-1*i]:
            is_palindorme = False
            break

    return is_palindorme


def is_palindorme_simple(text: str) -> bool:
    return text == text[::-1]


def sort(text: str, sort_type: str = 'asc') -> str:
    sort_types = ('asc', 'desc')
    if sort_type not in sort_types:
        raise ValueError('Wrong sort type')

    abc: str = 'abcdefghijklmopqrstuvwxyz'

    if sort_type == 'desc':
        abc = abc[::-1]

    unique_text: set = set(text)
    sorted_str: str = str()

    # n**2
    for letter in abc:
        for char in unique_text:
            if letter == char:
                sorted_str += letter
                continue

    return sorted_str


def sort_utf(text: str, sort_type: str = 'asc'):
    # Do setup
    sort_types = ('asc', 'desc')
    if sort_type not in sort_types:
        raise ValueError('Wrong sort type')

    unique_unicode_chars: set = set(ord(char) for char in text)
    is_reversed = sort_type == 'desc'

    # Do sort
    sorted_chars = sorted(unique_unicode_chars, reverse=is_reversed)

    # Do formatting
    sorted_chars = [chr(char) for char in sorted_chars]
    sorted_chars = ''.join(sorted_chars)
    return sorted_chars


print("asc sort")
print(sort_utf("abcs"))
print(sort_utf("5543234"))
print(sort_utf("абцдabc23"))

print("desc sort")
print(sort_utf("abcdejj", sort_type="desc"))
