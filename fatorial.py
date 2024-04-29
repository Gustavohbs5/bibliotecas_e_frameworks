fatorial = int(input("Digite o número: "))
numero = fatorial
multiplicador = fatorial

while multiplicador >= 2:
    multiplicador = multiplicador -1
    fatorial = fatorial * multiplicador
    if multiplicador == 2:
        print(f'O fatorial de {numero} é: {fatorial}')
    elif fatorial <= 2:
        print("O número que você digitou pequeno! Digite um número maior")







#import math

#fatorial = int(input("Número Que deseja Calcular: "))
#print(f'O fatorial de {fatorial} é: {math.factorial(fatorial)}')

#Output
# O fatorial de 5: é 120



