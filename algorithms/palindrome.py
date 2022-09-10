"""
Help Vasya understand if the phrase will be a palindrome. Only letters and numbers are counted,
uppercase and lowercase letters are considered the same.

The solution should run in O(N), where N is the length of the input string.

Input example:
A man, a plan, a canal: Panama
"""

def palindrome(text: str) -> bool:
    clean_text = ''.join(e.lower() for e in text if e.isalpha())
    clean_text_len = len(clean_text)
    return clean_text[:clean_text_len//2] in clean_text[clean_text_len//2:][::-1]


def read_input() -> str:
    text = str(input())
    return text


text = read_input()
print(palindrome(text))