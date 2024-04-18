#Criando o titulo de apresentação da calculadora
print("**********Calculadora em Python**********", '\n', "\nSelecione a opção desejada:")

#Gerando um loop para estrutura de repetição
while True:

    #Criando as opções de Soma, Subtração, Multiplicação, Divisão e Porcentagem
    print('1 - Soma', '\n2 - Subtração', '\n3 - Multiplicação', '\n4 - Divisão', '\n5 - Porcentagem', '\n')

    #Crindo input para fazer a pergunta desejada e condições de respostas
    opcao_operacao = int(input('Digite a opção desejada (1/2/3/4/5):'))
    if opcao_operacao >= 1 and opcao_operacao <= 5:
        perg1 = int(input('Digite o primeiro numero: '))
        perg2 = int(input('Digite o segundo numero: '))
    elif perg1 and perg2 is not int:
        print('Digite apenas numeros! ')
    else:
        print('Digite numeros entre 1 e 5!')

    #Criando condicionais para as repostas da opção de operação
    if opcao_operacao == 1:
        opSoma = int(perg1 + perg2)
        print('O resultado da soma é: {}' .format(opSoma))
    elif opcao_operacao == 2:
        opSub = int(perg1 - perg2)
        print('O resultado da subtração é: {}'.format(opSub))
    elif opcao_operacao == 3:
        opMulti = int(perg1 * perg2)
        print('O resultado da multiplicacao é: {}'.format(opMulti))
    elif opcao_operacao == 4:
        opDiv = int(perg1 // perg2)
        print('O resultado da divisao é: {}'.format(opDiv))
    elif opcao_operacao == 5:
        opPorc = int(perg1 * perg2 // 100)
        print('O resultado da porcentagem é: {}'.format(opPorc))
    #Pergunta de repetição e agradecimento
    exec_again = input(str("Deseja executar novamente? (sim/não): "))
    print('\n')
    if exec_again == 'não' or exec_again == 'nao':
        print('Obrigado por usar nossa calculadora!')
        break
