print("=== calculadora ===")
operacao = input("Digite a operação (+, -, *, /, **, ): ")

# valida se a operação digitada é suportada antes de pedir os números.
if operacao in ['+', '-', '*', '/', '**']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    elif operacao == '/':
        # impede erro de divisão por zero que quebraria o programa.
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
            resultado = None
    elif operacao == '**':
        resultado = num1 ** num2
        print(f"O resultado de {num1} ** {num2} é: {resultado}")
else:
    print("Operação inválida.")
print("=== Fim da calculadora ===")
print("enter para sair...")


