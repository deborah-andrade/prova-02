m = [[0, 0, 0], [0, 0, 0]]  #comecei criando a matriz com os números escolhidos pela pessoa.
for l in range(0, 2):
    for c in range(0, 3):
        m[l][c] = float(input(f'Digite um valor para [{l}, {c}]: '))         #usando for in range faz o cog ficar menor, não precisando utilizar append.
for l in range(0, 2):
    for c in range(0, 3):
        print(f'[{m[l][c]}]', end='')  #saida da matriz em tela.
    print()

e = float(input('Digite um valor real para a multiplicação: '))   #número real escoplhido pela pessoa para multiplicação.
print(f'O resultado da multiplicação do escalar {e} com a matriz foi:', end=' ')  #print antes do def para não haver repetição de frase a cada radada de def.

def multiplicação (matriz, escalar):
    mult = matriz * escalar
    print(mult, end=' ')       #funçao criada para multiplicar o escalar escolhido com cada elemento da matriz formada anteriormente.

multiplicação(m[0][0], e)
multiplicação(m[0][1], e)
multiplicação(m[0][2], e)
multiplicação(m[1][0], e)
multiplicação(m[1][1], e)
multiplicação(m[1][2], e)
