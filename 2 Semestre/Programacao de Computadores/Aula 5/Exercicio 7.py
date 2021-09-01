'''7.Faça um programa que leia uma data e determine se ela é válida, ou seja, 
verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro 
tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.Faça funções para 
validação e para verificar se o ano é bissexto.'''


import re


#------------#
def vali_data(data):
    return bool(re.match(r"\d{2}/\d{2}/\d{4}",data))


#------------#
def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    return False


#------------#
def main():
    data = ""
    while True:
        data = input("Digite a data: ")
        if vali_data(data): break
        print("Data Invalida. Digite a data no formato dd/mm/aaaa")

    data = map(int,data.split("/"))
    
    if bissexto(data[2]):
        if data[1] in [] :




















main()

     