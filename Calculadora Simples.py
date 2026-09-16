def calculadora():
    print("=== CALCULADORA ===")

    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = num1 + num2

    elif operador == "-":
        resultado = num1 - num2

    elif operador == "*":
        resultado = num1 * num2

    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            return

    else:
        print("Operação inválida!")
        return

    print(f"Resultado: {resultado}")


calculadora()