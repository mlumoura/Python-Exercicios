# pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# se c0 ≠ 1 , volte ao ponto 2.

c0 = int(input("Digite um numero: "))

etapas = 0

while c0 != 1:
    if c0 % 2 == 0: c0 = c0 / 2
    else: c0 = 3 * c0 + 1
    etapas += 1
    print(c0)
print(etapas)