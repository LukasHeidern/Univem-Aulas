def register():
    registry = open('registration-Ex2.txt','a',encoding = 'utf-8')
    while True:
        name = input("Digite o nome do atleta: ").capitalize()
        height = input("Digite a altura do atleta: ")
        weight = input("Digite o peso do atleta: ")

        registry.write(f"{name};{height};{weight}\n")

        if input("Deseja continuar? [S/n]: ")[0] not in "Ss": break
    registry.close()
    pass

def showmmc():
    for i in open('registration-Ex2.txt','r',encoding = 'utf-8').readlines():
        line = i.split(';')
        print(f"Atleta - {line[0]}\nMMC - {float(line[1]) / (float(line[2]) ** 2)}")
    pass

def main():
    while True:
        what = input(f"1 -  Registrar;\n"
                    f"2 - Mostrar todos\n;"
                    f"0 - Sair.\n"
                    f"Digite a opcao: ")

        if what == '0':
            print("saindo")
            break

        elif what == '1':
            register()

        elif what == '2':
            showmmc()

        else: print("Opcao invalida!")
    pass

main()







