n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maior = n1

if n2>n1: maior = n2
elif n3>maior: maior = n3

print("O maior número é:", maior)
