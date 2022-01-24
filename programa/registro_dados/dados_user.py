from random import randint
from re import sub


#função que cria um valor inteiro aleario para o id do usuário
def id_user():
    usuario = randint(1,100000)
    return usuario

#função que pede o nome do usuário a ser matriculado
def nome():
    while True:
        
        nome_user = input("Digite seu nome: ").upper()
        nome_user = sub("[^A-Za-zÀ-Úà-úÃ-Õã-õ ]", "", nome_user)
        try:
            nome_user =str(nome_user)
            if len(nome_user) <=50 and len(nome_user) >1:
                break
            else:
                print('Nome inválido tente novamente.')
                continue
        except ValueError as erro2:
            with open('doc_erro_cpf.txt', 'a+') as documentos:
                documentos.write(erro2,'\n')
    return nome_user



if __name__ =="__main__":
    print(id_user())
        
    
    
