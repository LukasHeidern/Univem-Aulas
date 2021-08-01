'''2) A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos 
de indústrias que são altamente poluentes do meio ambiente. O índice de poluição 
aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo 
são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as 
indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice 
atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. 
Faça um algoritmo que leia o índice de poluição medido e emita a notificação adequada 
aos diferentes grupos de empresas.'''

iPolucao = float(input("Digite o indice de poluicao: "))

if iPolucao < 0.25: print("Indice de poluicao dentro do limite aceitavel!")
elif iPolucao >= 0.3: print(f"Indice de poluicao acima do limite aceitavel! 1o grupo Deve suspender suas atividades")
elif iPolucao >= 0.4: print(f"Indice de poluicao acima do limite aceitavel! 1o e 2o grupo Devem suspender suas atividades")
elif iPolucao >= 0.5: print(f"Indice de poluicao acima do limite aceitavel! Todos os grupos Devem suspender suas atividades")