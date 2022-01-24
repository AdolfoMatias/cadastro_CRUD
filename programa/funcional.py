#bibliotecas puxadas das pastas

from registro_cpf.registrador_cpf import registro_cpf,procura_cpf
from registro_dados.dados_user import id_user, nome
from registro_dados.substituir import atualizar_info, deletar_info
#biblioteca time com a função dormir
from time import sleep

class Estudante:
    def __init__(self):
        self.__lista_cpf = []
        self.__lista_nome=[]
        self.__lista_id =[]
        #self.users ={}

    #settando listas 
    @property
    def lista_cpf(self):
        return self.__lista_cpf
    @property
    def lista_nome(self):
        return self.__lista_nome
    
    @property
    def lista_d(self):
        return self.__lista_id

    #função de matricular
    def matricular(self):
        print("---------------MATRICULAR---------------")
        full_name = nome()
        self.__lista_nome.append(full_name)

        while True:
            #função que recebe o cpf
            var_cpf =registro_cpf()
            if var_cpf not in self.lista_cpf:
                self.lista_cpf.append(var_cpf)
                break
            else:
                print('Este CPF já consta na nossa base de dados')
                return
        
        #grava o cpf na lista_cpf
        while True:
            with open ('lista_cpf.csv', 'a+') as doc2:
                doc2.seek(0)
                if str(var_cpf) not in doc2.read():
                    doc2.write(str(var_cpf)+'\n')
                    pass
                else:
                    print('CPF já consta na lista de matriculados')
                    return

            #cria uma id aleatória, caso chegue a um limite dispara uma aviso
            """A id precisa estar depois do cpf pois se for antes o id será registrado, mesmo tendo cpf duplicado isso ocorre 
            porque o id procura de forma aleatória até não se repetir, depois que acha dá um pass e se registra em lista_id, 
            mas o CPF não, o cpf duplicado se diz duplicado e fecha sem gravar. Isso porque o id é automatico na colocação e o CPF é manual"""
            var_id = id_user()
            with open ('lista_id.csv', 'a+') as doc1:
                doc1.seek(0)
                if str(var_id) not in doc1.read():
                    doc1.write(str(var_id)+'\n')
                    pass
                else:
                    print('ID chegou ao Limite')
                    return

            #Salva os arquivos no arquivo txt não se forem duplicados
            with open('user_id.csv', 'a+') as file:
                #abre o arquivo para conferir se tem algo repetido
                doc1 = open('lista_id.csv','r+')
                doc1.seek(0)
                file.seek(0)
                if str(var_id) not in doc1.readlines():
                    try:
                        with open ('user_id.csv', 'a+', encoding='utf-8') as file:
                            #utilizei um acréscimo ao valor de id com id+
                            file.write ('id'+str(var_id)+ ', '+ str(var_cpf) +', '+ full_name +'\n')
                        doc2.close()
                        doc1.close()
                        break
                    finally:
                            print(f'Matrícula registrada com sucesso.')
                else:
                    print('Duplicação ID ou CPF')
                    return


    #lista todos os matriculados
    def listar_matriculados(self):
        print("--------------MATRICULADOS-------------")
        with open('user_id.csv', 'r', encoding='utf-8') as listar:
            listar.seek(0)
            print('ID        CPF        NOME')
            for i in listar.readlines():
                
                if i.strip(','):
                    print(i.replace(',',''))
    
    #função que faz busca individual por CPF
    def listar_individual(self):
        print("------------BUSCANDO USUÁRIO--------------")
        dado_listado=0
        #busca o valor 
        with open('user_id.csv', 'r', encoding='utf-8') as listar:
            listar.seek(0)
            #procuro o cpf
            valor_cpf = procura_cpf()
            if len(valor_cpf) ==11:
                for i in listar.readlines():
                    #verifico se valor está em alguma linha(i) de todas linhas de listar
                    #i são todos os elementos tipo: id,cpf e nome, dai se valor_cpf estiver em algum:
                    if valor_cpf in i:
                        print('ID  ', '      CPF         ', '     NOME        ')
                        print(i)  
                        dado_listado = i
                               
            else:
                print("Valor inexistente")
                return
        return dado_listado

                            
    #função para deletar matriculado
    def delete_mat(self):
        sleep(0.5)
        print('--------------DESMATRICULAR---------------')
        #aqui verifico se o dado_listado é valor_rocurado se for zero não passa adiante a desmatricula, e se for diferente então ele tá na lista
        valor_procurado = self.listar_individual()
        #o self abaixo garente que ainda não deletei
        self.deletou = False
        if valor_procurado != 0:
            
            var_sub = deletar_info()
            # a função deletar_info() pergunta se quero deletar se for 1 então inicio o processo de delete:
            if var_sub==1:
                #Para deletar NÃO use o sinal de + no gerenciador de contexto(a+, r+ nem w+), pois ele irá dar append e não irá reescrever com w e sim com a+
                
                #BASE CENTRAL: user_id
                #leio user_id.csv com a saída listotal:
                with open('user_id.csv', 'r', encoding='utf-8') as listotal:
                    #a partir da linha 0:
                    listotal.seek(0)
                    #gravo todas linhas lidas pelo "r" de user_id em garvadortotal com o comando readlines(), gravei o conteúdo com o cpf procurado
                    gravadortotal = listotal.readlines()
                    # o truque de apagar está aqui, usar o "w" irá reescrever a gravação anterior
                    with open('user_id.csv', 'w', encoding='utf-8') as listotal2:
                        #verifico se o valor completo: id,cpf,nome(valor_procurado) está em alguma linha de user_id
                        if valor_procurado in gravadortotal:
                            for i in gravadortotal:
                                #se o valor procurado for diferente  de tudo então eu regravo em outra saida(listatotal2) sobrescrevendo o anterior
                                #pois significa que esse valor foi apagado
                                #eu regravo com o valor que é diferente do que eu procuro entendeu? assim digo: olha reescreve sem usar a linha procurada
                                if valor_procurado != i: # o i é a linha que não tem o que procuro, ou seja reescreva ela
                                    listotal2.write(i)

                    
                    #ATENÇÃO mantenha essa identação
                    #abaixo procuro nas listas_cpf e lista_id se eles não tiverem conteudo em user_id então eu reescrevo só com o que tiver em user_id
                    #assim 
                                                    
                    #Apagando ID na lista_id.csv
                    with open('lista_id.csv', 'r') as lisid:
                        lisid.seek(0)
                        #veja gravo tudo pois o w reescreve
                        gravadorid = lisid.readlines()
                        #crio uma nova saida como a lisid2 e reescrevo com o w
                        with open('lista_id.csv', 'w') as liscpf2:
                            for i in gravadorid:
                                #eu verifico se algum valor da lista_id está em alguma linha da lista user_id
                                if i in gravadortotal:
                                    liscpf2.write(i)

                    #Apagando cpf na lista_cpf.csv
                    with open('lista_cpf.csv', 'r') as liscpf:
                        liscpf.seek(0)

                        gravadorcpf = liscpf.readlines()

                        with open('lista_cpf.csv', 'w') as liscpf2:
                            for i in gravadorcpf:
                                #verifico se algum valor da lista_cpf está na lista user_id
                                if i in gravadortotal:
                                    liscpf2.write(i)
                #se deletei então garanto o true
                self.deletou=True
                print(f"Usuário de CPFnº {i}deletado com sucesso.")
            else:
                print('Ok usuário não deletado')
                return                               
        else:
            print('Aluno não matriculado')
            return

    # a função que atualiza os dados
    def atualizar(self):
        varnovo = atualizar_info()
        if varnovo ==1:
            sleep(0.5)
            print('----------------\nPrimeiro você precisará deletar a matrícula atual:\n---------------')
            sleep(0.5)
            #reaproveito a função delete
            self.delete_mat()
            sleep(0.5)
            #verifico se deletei observando lá em delet_mat era false ou True
            if self.deletou is True:
                #limpo a lista de cpf para não dar conflito em cpf já existente
                self.lista_cpf.clear()
                print('----------------\nSe deletou basta apenas MATRICULAR novamente:\n----------------')
                sleep(.5)
                #reparoveito a função matricular
                self.matricular()
        else:
            print('Ok atualização nao realizada.')
            return


if __name__ == "__main__":
    a1 = Estudante()
    #a1.matricular()
    #a1.listar_matriculados()
    #a1.listar_individual()
    #a1.atualizar()
    #a1.delete_mat()
    
   

