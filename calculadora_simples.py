
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
