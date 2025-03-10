
# Módulo 3: Lógica de Programação com Python

Este módulo tem como objetivo desenvolver a lógica de programação utilizando Python. Os alunos aprenderão a trabalhar com operadores aritméticos, relacionais e lógicos, além de estruturas de controle como condicionais (`if`, `elif`, `else`) e estruturas de repetição (`for`, `while`). Também serão introduzidos à manipulação de strings para aplicar os conceitos em programas práticos.

---

## 🎯 Objetivo do Módulo
- Desenvolver a lógica de programação utilizando Python.
- Trabalhar com operadores aritméticos, relacionais e lógicos.
- Aprender estruturas de controle como condicionais e loops.
- Aplicar os conceitos em programas práticos, como uma calculadora interativa.

---

## 🏗️ Estrutura da Aula

### 1. Revisão Rápida do Módulo 1 (10 minutos)
- **Resumo dos conceitos aprendidos**:
  - Variáveis e tipos de dados.
  - Manipulação de strings.
  - Estrutura básica de um programa Python.
- **Resolução de dúvidas sobre o Módulo 1**.

### 2. Operadores em Python (30 minutos)
- **Operadores Aritméticos**:
  - `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão).
  - `//` (divisão inteira), `%` (módulo), `**` (exponenciação).
  - Exemplo:
    ```python
    a = 10
    b = 3
    print(a + b)   # Soma -> 13
    print(a // b)  # Divisão inteira -> 3
    print(a ** b)  # Exponenciação -> 1000
    ```

- **Operadores Relacionais**:
  - `==` (igual), `!=` (diferente), `>` (maior), `<` (menor), `>=` (maior ou igual), `<=` (menor ou igual).
  - Exemplo:
    ```python
    print(a > b)  # True
    print(a == b)  # False
    ```

- **Operadores Lógicos**:
  - `and` (E), `or` (OU), `not` (NÃO).
  - Exemplo:
    ```python
    print(a > 5 and b < 5)  # True
    print(not (a > 5))  # False
    ```

### 3. Estruturas Condicionais (40 minutos)
- **Condicional `if`**:
  ```python
  idade = 18
  if idade >= 18:
      print("Você é maior de idade.")
  ```

- **Condicional `if-else`**:
  ```python
  if idade >= 18:
      print("Você é maior de idade.")
  else:
      print("Você é menor de idade.")
  ```

- **Condicional `if-elif-else`**:
  ```python
  nota = 7.5
  if nota >= 9:
      print("Excelente!")
  elif nota >= 7:
      print("Bom!")
  else:
      print("Precisa melhorar.")
  ```

### 4. Estruturas de Repetição (40 minutos)
- **Loop `for`**:
  ```python
  for i in range(5):
      print(f"Valor de i: {i}")
  ```

- **Loop `while`**:
  ```python
  contador = 0
  while contador < 5:
      print(f"Contador: {contador}")
      contador += 1
  ```

### 5. Manipulação de Strings (20 minutos)
- **Métodos úteis de strings**:
  - `upper()`, `lower()`, `strip()`, `replace()`, `split()`.
  - Exemplo:
    ```python
    frase = "Python é uma linguagem poderosa"
    for palavra in frase.split():
        print(palavra.upper())
    ```

### 6. Atividade Prática (40 minutos)
- **Criar uma calculadora simples**:
  ```python
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
  ```

### 7. Desafio Extra (20 minutos)
- **Criar um menu interativo usando `while`**:
  ```python
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
  ```

---

## 📂 Exemplos de Código

### 1. Operadores Aritméticos
**Arquivo:** `operadores_aritmeticos.py`
```python
a = 10
b = 3
print(a + b)  # 13
print(a // b)  # 3
print(a ** b)  # 1000
```

### 2. Condicional `if-elif-else`
**Arquivo:** `condicionais.py`
```python
nota = 7.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")
```

### 3. Loop `for`
**Arquivo:** `loop_for.py`
```python
for i in range(5):
    print(f"Valor de i: {i}")
```

### 4. Loop `while`
**Arquivo:** `loop_while.py`
```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```

### 5. Calculadora Simples
**Arquivo:** `calculadora_simples.py`
```python
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
```

---

## 🛠️ Projeto Prático

### Descrição
Desenvolver uma calculadora interativa com operações básicas (soma, subtração, multiplicação, divisão) e personalização.

### Checklist de Entrega
- [ ] Programa da calculadora simples.
- [ ] Uso de condicionais (`if`, `elif`, `else`) para escolher a operação.
- [ ] (Desafio) Uso de `while` para criar um menu interativo.
- [ ] Código enviado para o repositório GitHub na pasta `Modulo_03/`.

---

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

