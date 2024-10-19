"""функциюя, которая принимает на вход строку и возвращает ее со всеми заглавными буквами."""
def upper_word(str):
    return str.upper()

"""функция, которая делает заглавными первые буквы каждого слова в строке"""
def word(str):
    return ' '.join(word.capitalize() for word in str.split())
