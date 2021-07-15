'''5) Escreva um algoritmo que leia um tempo em segundos e calcule o total de 
horas, minutos e segundos  equivalentes a este tempo dado de entrada.	
Por exemplo: 7850 segundos é igual a: 2 horas 10 minutos e 50 segundos. '''


segundos = int(input("Digite o total de segundos: "))
h = segundos // 3600
m = (segundos % 3600) // 60
s = (segundos % 3600) % 60
print(f"{h}:{m}:{s} horas")