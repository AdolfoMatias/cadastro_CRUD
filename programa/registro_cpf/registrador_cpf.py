from re import sub
cpf_add =[]
#essa função calcula os valores de digitos de cpf
def calculator(elemento):
    val1= 0
    val2= 0

    #calculo do primeiro digito
    mantenedor = 0
    while  mantenedor < 9:
        val1 =0
        for i in enumerate(reversed(elemento[0:9]), start=2):
            i = int(i[0])*int(i[1])
            val1+=i

            mantenedor += 1   

    val1 = val1%11
   
    val1 = 11-val1
    

    #calculo do segundo digito do cpf
    mantenedor = 0
    while  mantenedor < 10:
        for i in enumerate(reversed(elemento[0:10]), start=2):
            i = int(i[0])*int(i[1])
            val2+=i
            mantenedor += 1
    val2= val2%11
    val2 = 11-val2
    valores = [val1,val2]
    return valores
    
# aqui se tem a validação dos valores atingidos pelos digitos, 
def digitando(funcao, elemento, verificador):
    x,y = funcao(elemento)
    if x < 10:
        pass
    else:
        x =0
    if y <10:
        pass
    else:
        y=0
    
    if x == int(elemento[9]) and y == int(elemento[10]):
        print(f'{verificador} é um CPF válido')
    else:
        print(f'{verificador} é um CPF inválido')
        print(x,y)

    

#aqui se faz a imputação dos dados gerais do cpf do matriculado
def registro_cpf():
    while True:
        digitos = input('Digite seu CPF: ')
        digitos1 = digitos
        #sub remove tudo que tiver fora do ^0-9
        digitos = sub("[^0-9]", "", digitos)
    
        try:
            
            if len(digitos) == 11:
                #valirador multiplica para garantir um valor diferente de ex.: 111.111.111-11
                validador = digitos[0]*9
                if digitos[0:9] != validador:
                    [cpf_add.append(x) for x in digitos]
                    calculator(cpf_add)
                    digitando(calculator,cpf_add, digitos1)
                else:
                    print('Valor errado')
                    continue

                break
            else:
                print('Valor incorreto')
                continue

        except ValueError as erro1:
            with open('doc_erro_cpf.txt', 'a+') as documentos:
                documentos.write(erro1,'\n')
    return digitos


#funçãoq ue procura 11 digitos para procurar na busca por usuário matriculado no programa principal main.py
def procura_cpf():
    while True:
        pcpf = input('Digite os números do CPF: ')
        pcpf = sub("[^0-9]", "",pcpf)
        try:
            if len(pcpf) ==11:
                pcpf=str(pcpf)
                break
            else:
                print('CPF inválido')
                continue
        except ValueError as erro:
            print("Erro de valor")

    return pcpf



#teste
if __name__ =="__main__":

    registro_cpf()
    # elemento = [0,9,5,0,3,2,4,5,4,0,0]
    # val1= 0
    # val2= 0

    # mantenedor = 0
    # while  mantenedor <9:
    #     val1 =0
    #     for i in enumerate(reversed(elemento[0:9]), start=2):
    #         i = int(i[0])*int(i[1])
            
    #         #print(f'{int(i[0])}* {int(i[1])}')
    #         val1+=i
    #         print(val1)
            

    #         mantenedor += 1   
    #     print(mantenedor)