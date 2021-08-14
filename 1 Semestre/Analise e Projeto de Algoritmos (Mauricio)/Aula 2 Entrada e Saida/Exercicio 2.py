'''2) elabore um algoritmo que leia as medidas de um terreno retangular
(comprimento e largura) e calcule e mostre qual e o perimetro e qual e a 
area do terreno. '''

comp = float(input("Digite o valor do comprimento do terreno: "))
larg = float(input("Digite o valor da largura do terreno: "))

area = larg * comp
per =  larg * 2 + comp * 2

print(f"O perimetro e {per} e a area e {area}")
