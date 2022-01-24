from funcional import Estudante
from re import sub
from time import sleep

# crio uma classe que herda de Estudante
class Execut(Estudante):
    def __init__(self):
        super().__init__()
        
 

    #Crio as opções de 1 a 6 dando as opçoes da lista
    def optativo(self):
        while True:
            print("--------------ESCOLA CRUD----------------")
            print("-----------------------------------------")
            sleep(0.5)
            opcoes = input("""Digite o número da opção desejada: 

            1 - Matricular
            2 - Buscar Matrícula  
            3 - Todas Matrículas
            4 - Atualizar Matrícula
            5 - Deletar Matrícula
            6 - Nada          
            
-----------------------------------------
Opção desejada: """)
#todas essa funções são herdade da classe Estudante
            try:
                opcoes = int(opcoes)
                if opcoes >=1 or opcoes <=6:
                    if opcoes ==1:
                        self.matricular()
                        break
                    elif opcoes ==2:
                        self.listar_individual()
                        break
                    elif opcoes ==3:
                        self.listar_matriculados()
                        break
                    elif opcoes ==4:
                        self.atualizar()
                        break
                    elif opcoes ==5:
                        self.delete_mat()
                        break
                    elif opcoes ==6:
                        print("Ok, encerrando.")
                        return
                
                else:
                    print('Você digitou um valor inválido tente novamente de 1 a 6.')
                    continue
            except ValueError as errop1:
                print('Formato de valor inválido')
            except  TypeError as errop2:
                print('Formato não suportado')


     #A função receve a função anterior e após a primeira execução entra em loop de perguntar se querp continuar as ções da função optativo()
    def cont_op(self):
        self.optativo()
        while True:
            
            
            sleep(1)
            print("-----------------------------------------")
            opcao_c = input("Deseja continuar? S/n: ").upper()
            opcao_c = sub("[^SN]", "", opcao_c)
            try:
                if opcao_c =="S" or opcao_c =="N":
                    if opcao_c == "S":
                        self.optativo()
                    else:
                        print("Finalizando")
                        break

                else:
                    print("Formato inválido digite só S para sim ou N para não")
                    continue
            except TypeError as errop3:
                print("Erro de valor")
      



if __name__ == "__main__":

    #instancioo crud e o executo
    iniciar_crud = Execut()  
    iniciar_crud.cont_op()

