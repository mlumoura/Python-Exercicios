# Crie um programa com um loop for e uma declaração continue.
# O programa deve repetir uma sequência de dígitos, substituir cada 0
# por x e imprimir a sequência modificada na tela.
# Use o esqueleto abaixo:
texto = ""

for digit in "0165031806510":
    if digit == "0":
        texto = texto + "x"
    else: texto = texto + digit
print (texto)