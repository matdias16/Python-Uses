import math

# Funções das operações
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


def potencia(a, b):
    return a ** b


def raiz(a):
    if a < 0:
        return "Erro: não existe raiz quadrada real de número negativo!"
    return math.sqrt(a)


def seno(angulo):
    return math.sin(math.radians(angulo))


def cosseno(angulo):
    return math.cos(math.radians(angulo))


# Programa principal
while True:
    print("\n===== CALCULADORA CIENTÍFICA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Seno")
    print("8 - Cosseno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Calculadora encerrada.")
        break

    elif opcao in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", soma(num1, num2))

        elif opcao == "2":
            print("Resultado:", subtracao(num1, num2))

        elif opcao == "3":
            print("Resultado:", multiplicacao(num1, num2))

        elif opcao == "4":
            print("Resultado:", divisao(num1, num2))

        elif opcao == "5":
            print("Resultado:", potencia(num1, num2))

    elif opcao == "6":
        num = float(input("Digite um número: "))
        print("Resultado:", raiz(num))

    elif opcao == "7":
        angulo = float(input("Digite o ângulo em graus: "))
        print("Resultado:", seno(angulo))

    elif opcao == "8":
        angulo = float(input("Digite o ângulo em graus: "))
        print("Resultado:", cosseno(angulo))

    else:
        print("Opção inválida!")