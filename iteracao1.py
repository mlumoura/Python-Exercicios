nome = ""

for ch in "john.smith@pythoninstitute.org":

    if ch == "@":
        break
    nome = nome + ch
print(nome)