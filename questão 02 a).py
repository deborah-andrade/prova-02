b = input("Digite um número em Binario: ")


def binarioparadecimal(n):    #defini a função.
    return int(n, 2)          #fiz um retorno para voltar como inteiro.


if __name__ == '__main__':                  #usei if __name__ com ajuda de aulas e sites explicativos.
    print('O resultado será:', binarioparadecimal(b))
