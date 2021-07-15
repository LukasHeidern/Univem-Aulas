'''3) Um motorista deseja colocar no seu tanque X reais de gasolina.
Escreva um algoritmo para ler o preco da gasolina e o valor do pagamento e 
exibir quantos litros ele conseguiu colocar no tanque.'''

preco = float(input("Digite o valor do Litro da gasolina: "))
pag = float(input("Quantos de gasolina deseja colocar (em reais): "))

litros = pag/preco

print(f"Com R${pag} voce colocou {litros:.2f} litros!")


