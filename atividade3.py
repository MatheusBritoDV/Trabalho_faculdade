opcoes = '''\n----- MENU PRINCIPAL -----\n
(1) Gerenciar Estudantes.
(2) Gerenciar Disciplinas.
(3) Gerenciar Professores.
(4) Gerenciar Turmas.
(5) Gerenciar Matrículas.
(9) Sair.\n'''
operacao_nao_encontrada = '\nEssa operação nao foi encontrada!\n'
incluir = '\n===== INCLUIR =====\n'
listar = '\n===== LISTAR =====\n'
atualizar = '\n===== ATUALIZAR =====\n'
exluir = '\n===== EXCLUIR =====\n'

while True:
    print(opcoes)
    opcao_escolhida = int(input('Informe a opcao desejada: '))
    if 1 <= opcao_escolhida <= 5 :
        if opcao_escolhida == 1:
            nome_opcao = 'ESTUDANTE'
        elif opcao_escolhida == 2:
            nome_opcao = 'DICIPLINAS'
        elif opcao_escolhida == 3:
            nome_opcao = 'PROFESSORES'
        elif opcao_escolhida == 4:
            nome_opcao = 'TURMAS'
        elif opcao_escolhida == 5:
            nome_opcao = 'MATRÍCULAS'
        while True:
            operacao = f'''\n***** [{nome_opcao}] MENU DE OPERAÇÕES *****\n
(1) Incluir.
(2) Listar.
(3) Atualizar.
(4) Excluir.
(9) Voltar ao menu principal.\n'''
            if opcao_escolhida == 1:
                print(operacao)
                operacao_escolhida = int(input('Informe a ação desejada: '))
                if operacao_escolhida == 1:
                    print(incluir)
                elif operacao_escolhida == 2:
                    print(listar)
                elif operacao_escolhida == 3:
                    print(atualizar)
                elif operacao_escolhida == 4:
                    print(exluir)
                elif operacao_escolhida == 9:
                    break
                else:
                    print(operacao_nao_encontrada)    
            elif opcao_escolhida == 2:
                    print(operacao)
                    operacao_escolhida = int(input('Informe a ação desejada: '))
                    if operacao_escolhida == 1:
                        print(incluir)

                    elif operacao_escolhida == 2:
                        print(atualizar)

                    elif operacao_escolhida == 3:
                        print(listar)

                    elif operacao_escolhida == 4:
                        print(exluir)

                    elif operacao_escolhida == 9:
                        break
                    else:
                        print(operacao_nao_encontrada)
            elif opcao_escolhida == 3:
                    print(operacao)
                    operacao_escolhida = int(input('Informe a ação desejada: '))
                    if operacao_escolhida == 1:
                        print(incluir)

                    elif operacao_escolhida == 2:
                        print(listar)

                    elif operacao_escolhida == 3:
                        print(atualizar)

                    elif operacao_escolhida == 4:
                        print(exluir)

                    elif operacao_escolhida == 9:
                        break
                    else:
                        print(operacao_nao_encontrada)
            elif opcao_escolhida == 4:
                    print(operacao)
                    operacao_escolhida = int(input('Informe a ação desejada: '))
                    if operacao_escolhida == 1:
                        print(incluir)

                    elif operacao_escolhida == 2:
                        print(listar)

                    elif operacao_escolhida == 3:
                        print(atualizar)

                    elif operacao_escolhida == 4:
                        print(exluir)

                    elif operacao_escolhida == 9:
                        break
                    else:
                        print(operacao_nao_encontrada)
            elif opcao_escolhida == 5:
                print(operacao)
                operacao_escolhida = int(input('Informe a ação desejada: '))
                if operacao_escolhida == 1:
                    print(incluir)

                elif operacao_escolhida == 2:
                    print(listar)

                elif operacao_escolhida == 3:
                    print(atualizar)

                elif operacao_escolhida == 4:
                    print(exluir)

                elif operacao_escolhida == 9:
                    break
                else:
                    print(operacao_nao_encontrada)
    if 5 < opcao_escolhida < 9:
        print(operacao_nao_encontrada)
    elif opcao_escolhida == 9:
        print('\nFinalizando programa\n')
        break
