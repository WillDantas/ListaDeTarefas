num1 = 0
num2 = 0
resultado = 0
op = ''

while True:
    num1 = float(input('Digite o primeiro numero:: '))
    op = input('Digite a operação matematica a ser feita: ')
    num2 = float(input('Digite o segundo numero:: '))

    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '/':
        resultado = num1 / num2
    elif op == '*':
        resultado = num1 * num2
    else:
        print('Operação não reconhecida!')

    print('{} {} {} = {}'.format(num1, num2, op, resultado))
