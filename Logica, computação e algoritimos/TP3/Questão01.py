#QUESTÃO 1 - Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Laço de execução da aplicação
while True:
    
    #Retorna erros
    try:
        
        #Entrada do total gasto
        total = float(input("Informe o valor total do consumo: R$ "))
        
        #Verificação do total
        if total > 0:

            #Entrada da quantidade de clientes
            clientes = int(input("Informe o total de clientes: "))
            
            #Verificação do número de clientes
            if clientes >= 1:

                #Entrada da taxa de serviço
                percentual = float(input("Informe o percentual do serviço, entre 0 e 100: "))
                
                #Verificação da taxa de serviço
                if percentual >=0 and percentual <=100:

                    #Tratamento dos valores
                    totalConsumo = float(total + (total * percentual / 100))
                    totalClientes = float(totalConsumo / clientes)
                    totalConsumo = ("%0.2f" % totalConsumo).replace(".", ",")
                    totalClientes = ("%0.2f" % totalClientes).replace(".", ",")

                    #Onde é impresso p resultado da aplicação
                    print(f"O valor total da conta, incluindo a taxa de serviço, será de R$ {totalConsumo}.\n")
                    print(f"Dividindo a conta por {clientes} clientes, cada cliente deve pagar R$ {totalClientes}.")
                
                #Onde é impresso o erro de porcentagem
                else:
                    print('A porcentagem deve ser entre "0" e "100".')
            
            #Onde é impresso o erro de pessoas
            else:
                print("Valor inválido. Necessário ao menos uma pessoa.")
        
        #Onde é impresso o valor total
        else:
            print("Você precisa ter consumido!")
        
        #Entrada de continuidade
        print("\n----------------------------------------------------------------------------------")
        prossegue = input('Pressione "ENTER" para continuar ou "F" para finalizar. ')

        #Varificação de continuidade
        if prossegue == 'f' or prossegue == 'F':
            print('Finalizando...\n\nFim!')
            print("----------------------------------------------------------------------------------")
            break
    
    #Aviso de erro
    except ValueError:
        print("\nEntrada inválida \n")