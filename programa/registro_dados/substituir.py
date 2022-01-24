#crio opções a serem chamandas na função principal, essa aqui permite o suário escolher deletar ou não
def deletar_info():
    op1 = 0
    while True:
        op_subs= input("""--------------DESVINCULAR----------------
        1 - Deletar matrícula
        2 - Nada
        Opção: """)
        try:
            op_subs = int(op_subs)
            if op_subs == 1:
                op1 = 1
                break
            elif op_subs ==2:
                return
            else:
                print('Valor inválido.')
                continue
        except ValueError as erro_subs:
            print('Valor errado, tente novamente')
    return op1

#também a ser chamanda na função principal, essa aqui permite o suário escolher atualizar ou não
def atualizar_info():
    op1 = 0
    while True:
        op_subs= input("""---------------ATUALIZAR-----------------
        1 - Atualizar dados de alunos
        2 - Nada
        Opção: """)
        try:
            op_subs = int(op_subs)
            if op_subs == 1:
                op1 = 1
                break
            elif op_subs ==2:
                return
            else:
                print('Valor inválido.')
                continue
        except ValueError as erro_subs:
            print('Valor errado, tente novamente')
    return op1


if __name__=="__main__":
    ...

            
