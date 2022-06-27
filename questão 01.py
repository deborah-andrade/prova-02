x = input('Digite uma frase: ')

from random import choice


def StringMaluca(texto):
    print(''.join(choice((str.upper, str.lower))(char) for char in texto))
StringMaluca(x)
StringMaluca(x) 
StringMaluca(x)
