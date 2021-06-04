#QUESTÃO 3 - Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

#Laço da aplicação
while True:    

    #Retorna erros
    try:
        
        #Entrada da quantidade de participantes
        quantidade_part = int(input("Quantos participantes teve o concurso? "))

        #Laço de entrada de participante e notas
        for contador in range(quantidade_part):
            #Entrada do participante
            participante = input(f"Informe nome do {contador + 1}º participante: ")

            #Entrada da nota
            nota = float(input(f"Informe nota do {contador + 1}º participante: "))
            
            #Verificação de nota do participante
            if nota >=0  and nota <=10:
                if contador == 0 or nota > nota_ganhadora:
                    ganhador = participante
                    nota_ganhadora = nota

            #Laço de verificação de nota
            while nota <0 or nota > 10:
                print('\nA nota deve ser maior que "0" e menor que "10" \n')
                nota = float(input(f"Informe nota do {contador + 1}º participante: "))
                if nota >=0  and nota <=10:
                    if contador == 0 or nota > nota_ganhadora:
                        ganhador = participante
                        nota_ganhadora = nota

        #Onde é impresso o resultado da aplicação                
        print(f"\nO(a) vencedor(a) foi {ganhador} com nota {nota_ganhadora}!")
        print("----------------------------------------------------------------------------------")
       
        #Entrada de continuidade
        prossegue = input('Pressione "ENTER" para continuar ou "F" para finalizar. ')

        #Verificação de continuidade
        if prossegue == 'f' or prossegue == 'F':
            print('Finalizando...\n\nFim!')
            break
        else:
            print("----------------------------------------------------------------------------------")
            continue

    #Aviso de erro
    except ValueError:
        print('Entrada invalida.\n')

        #Entrada de continuidade 2
        prossegue2 = input('Pressione "ENTER" para reiniciar ou "F" para finalizar. ')

        #Verificação de continuidade
        if prossegue2 == 'f' or prossegue2 == 'F':
            print('Finalizando...\n\nFim!')
            break
        else:
            print("----------------------------------------------------------------------------------")
            continue