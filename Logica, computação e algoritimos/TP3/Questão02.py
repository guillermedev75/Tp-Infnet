#QUESTÃO 2 - Desenvolva uma aplicação que recebe a idade de uma pessoa e informe se essa pessoa pode votar ou não

#Laço de execução da aplicação
while True:

    #Retorna erros
    try:

        #Entrada da idade da pessoa
        idade = int(input("Informe a idade: "))

        #Verficação da idade
        if idade <1:
            print("Idade deve ser superior a 1.\n")
        else:

            #Verificação de obrigatoriedade de voto
            if idade >= 18 and idade < 70:
                print("Tem obrigação de votar.\n")

            #Verificação de não obrigatoriedade de voto
            elif idade == 16 or idade == 17 or idade >= 70:
                print("Não tem obrigação de votar.\n")
            else:

                #Vericação de capacidade de voto
                if idade < 16:
                    print("Não tem direito a voto.\n")
        #Entrada de continuidade
        print("----------------------------------------------------------------------------------")
        prossegue = input('Pressione "ENTER" para continuar ou "F" para finalizar. ').upper()

        #Verificação de continuidade
        if prossegue == 'F':
            print('Finalizando...\n\nFim!')
            break
        else:
            print("----------------------------------------------------------------------------------")
            continue
    #Aviso de erro
    except ValueError:
        print("A algum erro nos dados!\n----------------------------------------------------------------------------------\nReiniciando aplicação...\n")