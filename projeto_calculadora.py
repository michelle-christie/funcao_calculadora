n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = int(input('Escolha a operação: (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): '))


def calculadora(n1, n2, op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        if n2 != 0:
            return n1 / n2
        else:
            return "Divisão por zero não é permitida para essa operaçao."
    else:
        return 0

resultado = calculadora(n1, n2, op)
print(f'O resultado da operação é: {resultado}')
