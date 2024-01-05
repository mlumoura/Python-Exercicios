word_without_vowels = ""

# Solicitar ao usuário que digite uma palavra
# e atribua-o à variável user_word.

# Imprima a palavra atribuída a word_without_vowels.

user_word = input("Digite ua palavra: ")

user_word = user_word.upper()

for letter in user_word:
    # Preenchao corpo do loop for.
    if letter =="A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
        continue
    word_without_vowels = word_without_vowels + letter
print(word_without_vowels  )