import os


def converter(operation, valor): #<----- Função de conversão
    if operation == 1:
        result = int(valor, base=2)
        return result
    else:
        valor = int(valor)
        return bin(valor)[2:]


os.system('cls') or None  # limpeza do terminal

cont = 0
while cont < 1:
    # Menu do sistema
    print('\n--- Conversor de numero Binario ---\n')
    print('---      Escolha a operação     ---')
    print('---      1: Bin ----> Dec       ---')
    print('---      2: Dec ----> Bin       ---')
    print('---      3: Sair do programa    ---\n')

    operation = int(input("Digite a operação: "))
    print()

    if operation == 1: #<---- Validador de operação
        os.system('cls') or None
        valor = str(input("Digite o valor: "))
        
        valor_int = list(valor)#<----validando o binario
        bin = True
        for num in valor_int:
            if num != "0" and num != "1":
                bin = False #<----Fim validador

        if bin == True:
            print()
            print("O valor {} convertido é {} \n".format(valor, converter(operation, valor)))
        else:
            print("Valor Invalido")

    elif operation == 2:
        os.system('cls') or None
        valor = int(input("Digite o valor: "))
        print()
        print("O valor {} convertido é {} \n".format(valor, converter(operation, valor)))

    elif operation == 3:
        os.system('cls') or None
        cont += 1
        print("---     Fim do programa!   ---")

    else:
        os.system('cls') or None
        print("Operação invalida\n") #<---- Fim do validador de operação
