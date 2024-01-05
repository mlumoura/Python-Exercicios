# Sua tarefa é escrever um programa que lê o número de
# blocos que os construtores têm e gera a altura da pirâmide
# que pode ser construída usando esses blocos.

# Nota: a altura é medida pelo número de camadas totalmente concluídas;
# se os construtores não tiverem um número suficiente de blocos e não
# puderem concluir a próxima camada, eles terminarão seu trabalho
# imediatamente.

# Exemplo de entrada: 20
# Saída prevista:A altura da pirâmide: 5
#
# Exemplo de entrada:1000
# Saída prevista:A altura da pirâmide: 44


blocks = int(input("Insira o número de blocos:"))
# Escreva seu código aqui.
andar = 0
altura = 0
bloco = 0
total_blocos = 0

for andar in range(1, blocks):
    print(altura, bloco, total_blocos)
    bloco += 1
    total_blocos += bloco
    if total_blocos > blocks: break
    altura += 1

print("A altura da pirâmide:", altura)
