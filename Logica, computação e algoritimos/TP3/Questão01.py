#QUESTÃO 1 - Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Laço de execução da aplicação
while True:
    
    #Retorna erros
    try:
        
        #Variaveis
        total = float(input("Informe o valor total do consumo: R$ "))
        
        #Verificação do total
        if total > 0:
            pessoas = int(input("Informe o total de pessoas: "))
            
            #Verificação do número de pessoas
            if pessoas >= 1:
                percentual = float(input("Informe o percentual do serviço, entre 0 e 100: "))
                
                #Verificação da taxa de serviço
                if percentual >=0 and percentual <=100:
                    totalConsumo = float(total + (total * percentual / 100))
                    totalPessoa = float(totalConsumo / pessoas)
                    totalConsumo = ("%0.2f" % totalConsumo).replace(".", ",")
                    totalPessoa = ("%0.2f" % totalPessoa).replace(".", ",")

                    #Onde é impresso p resultado da aplicação
                    print(f"O valor total da conta, com a taxa de serviço, será de R$ {totalConsumo}.\n")
                    print(f"\033[1mDividindo a conta por {pessoas} pessoa(s), cada pessoa deverá pagar R$ {totalPessoa}.\033[m")
                
                #Onde é impresso o erro de porcentagem
                else:
                    print('\033[0;31mA porcentagem deve ser entre "0" e "100".\033[m')
            
            #Onde é impresso o erro de pessoas
            else:
                print("\033[0;31mValor inválido. Necessário ao menos uma pessoa.\033[m")
        
        #Onde é impresso o valor total
        else:
            print("\033[0;31mVocê precisa ter consumido!\033[m")
        
        #Entrada de continuidade
        print("\n----------------------------------------------------------------------------------")
        prossegue = input('Pressione "\033[0;31mENTER\033[m" para continuar ou "\033[0;31mF\033[m" para finalizar. ')

        #Varificação de continuidade
        if prossegue == 'f' or prossegue == 'F':
            print('Finalizando...\n\nFim!')
            print("----------------------------------------------------------------------------------")
            break
    
    #Aviso de erro
    except ValueError:
        print("\033[0;31m \nEntrada inválida\033[m \n")