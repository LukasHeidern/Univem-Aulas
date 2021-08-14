'''5.O código de  César é uma  das  mais  simples  e  conhecidas  técnicas  de  
criptografia. É um tipo  de substituição na  qual  cada  letra  do  texto é substituída  
por  outra,  que  se  apresenta  no  alfabeto abaixo  dela  um  número  fixo  de  vezes.  
Por  exemplo,  com  uma  troca  de  três posições, ‘A’ seria substituído por ‘D’, ‘B’ 
se tornaria ‘E’, e assim por diante. Implemente um programa que faça uso  desse  
Código  de  César  (3  posições),  entre  com  uma  string  e retorne  a  string codificada. 
Exemplo: 

String: a ligeira raposa marrom saltou sobre o cachorro cansado 
Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR'''

### a = 97 ---> z = 122

sermo = list(input("Digite uma palavra:"))
for i,p in enumerate(sermo):
    sermo[i] = chr((ord(p)) + 3)
sermo = "".join(sermo)
print(f"Nova string: {sermo}")

'''
string = input("Digite uma string: ")
print(f"String: {string}")
string = list(string)
for i,c in enumerate(string):
    string[i] = chr( ord(c) + 3 ) 
'''
