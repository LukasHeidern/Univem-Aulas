'''3) Elabore um algoritmo que leia a velocidade máxima permitida em uma 
rodovia e também a velocidade que um determinado veículo trafega. Verificar 
se ele sofrerá multa (caso em que sua velocidade seja superior a permitida) 
ou não. '''

v_max = float(input("Digite a velocidade maxima permitida: "))
v_traf = float(input("Digite a velocidade que esta trafegando: "))

if v_traf > v_max: print("Velocidade muito alta, voce sofrera uma multa!")
else: print("Dentro da velocidade maxima permitida!")
