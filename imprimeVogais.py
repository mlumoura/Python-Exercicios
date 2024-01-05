# Solicita que o usuário insira uma palavra
# e atribua-a à variável user_word.
user_word = input("Digite ua palavra: ")

user_word = user_word.upper()

for letter in user_word:
    # Preenchao corpo do loop for.
    if letter !="A"and letter !="E" and letter !="I" and letter !="O" and letter !="U":
        continue
    print(letter)
