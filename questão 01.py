x = input('Digite uma frase: ') 

from random import choice #impotei da biblioteca random so o que eu queria usar, que no caso era choice.


def StringMaluca(texto):     #criei a função e a defini
    print(''.join(choice((str.upper, str.lower))(char) for char in texto))  #usei choice para fazer a escolha das letras, usei as funções de str e por fim
StringMaluca(x)                                                              #usei char para percorer pela frase escolhida pela estrutura for.
StringMaluca(x) 
StringMaluca(x)
