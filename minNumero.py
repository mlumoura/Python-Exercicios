# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.

menor = min(number1, number2, number3)

# Imprimir o resultado.
print("O menor número é:", menor)
