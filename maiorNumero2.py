# Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprimir o resultado
print("O maior número é:", larger_number)


# se qualquer uma das ramificações if-elif-else contiver apenas uma instrução,
# não é necessário criar uma linha recuada após a palavra-chave,
# mas apenas continuar a linha após os dois pontos.