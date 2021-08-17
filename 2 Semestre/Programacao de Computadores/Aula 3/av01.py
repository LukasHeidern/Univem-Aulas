#Avaliaçao 01 Aula 3

pronomes = ["do","da","dos","das"]
nome = input("Digite o nome completo:")
print(f"Nome Completo sem a conversao: {nome}")
nome = nome.split()
for i in range(len(nome)):
    if nome[i] not in pronomes:
        nome[i] = nome[i].capitalize()
nome = " ".join(nome)
print(f"Nome Completo com a conversao: {nome}")
