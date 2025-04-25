quantidade = int(input("Digite quantos números você quer inserir: "))
soma = 0
maximo = None
minimo = None

if quantidade >= 1:
    numero1 = float(input("Digite o primeiro número: "))
    soma += numero1
    maximo = numero1
    minimo = numero1

if quantidade >= 2:
    numero2 = float(input("Digite o segundo número: "))
    soma += numero2
    if numero2 > maximo:
        maximo = numero2
    if numero2 < minimo:
        minimo = numero2

if quantidade >= 3:
    numero3 = float(input("Digite o terceiro número: "))
    soma += numero3
    if numero3 > maximo:
        maximo = numero3
    if numero3 < minimo:
        minimo = numero3

if quantidade >= 4:
    numero4 = float(input("Digite o quarto número: "))
    soma += numero4
    if numero4 > maximo:
        maximo = numero4
    if numero4 < minimo:
        minimo = numero4

media = soma / quantidade

print('a média do número é {}'.format(média))
print('a soma do número é {}'.format(soma))
print('o número mínimo é {}'.format(mínimo))
print('o número máximo é {}'.format(máximo))
