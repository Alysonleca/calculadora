
print('Iniciando calculadora...')
print('')

def calculadora():
        operacao = input('Qual operacao deseja fazer?: ')
        val1 = int(input('Apresente o primeiro valor: '))
        val2 = int(input('Apresente o segundo valor: '))
        if operacao == '+':
            resultado = val1 + val2
        elif operacao == '-':
            resultado = val1 - val2
        elif operacao == '*':
            resultado = val1 * val2
        elif operacao == '/':
            resultado = val1 / val2
        print(resultado)
        loop()

def loop():
    validacao = input('Deseja fazer uma nova conta?')
    if validacao == 'Sim':
        calculadora()
    elif validacao == "Nao":
        print('Finalizando')
    else:
        loop()

calculadora()






