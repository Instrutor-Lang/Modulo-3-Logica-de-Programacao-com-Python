# operadores_aritmeticos.py
a = 10
b = 3
print(a + b)  # 13
print(a // b)  # 3
print(a ** b)  # 1000

# operadores_relacionais.py
print(a > b)  # True
print(a == b)  # False

# operadores_logicos.py
print(a > 5 and b < 5)  # True
print(not (a > 5))  # False

# condicional_if.py
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# condicional_if_else.py
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# condicional_if_elif_else.py
nota = 7.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")

# loop_for.py
for i in range(5):
    print(f"Valor de i: {i}")

# loop_while.py
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# manipulacao_strings.py
frase = "Python é uma linguagem poderosa"
for palavra in frase.split():
    print(palavra.upper())

# calculadora_simples.py
print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print(f"Resultado: {num1 + num2}")
elif opcao == '2':
    print(f"Resultado: {num1 - num2}")
elif opcao == '3':
    print(f"Resultado: {num1 * num2}")
elif opcao == '4':
    print(f"Resultado: {num1 / num2}")
else:
    print("Opção inválida!")

# calculadora_interativa.py
while True:
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação: ")

    if opcao == '5':
        print("Saindo...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcao == '2':
        print(f"Resultado: {num1 - num2}")
    elif opcao == '3':
        print(f"Resultado: {num1 * num2}")
    elif opcao == '4':
        print(f"Resultado: {num1 / num2}")
    else:
        print("Opção inválida!")
