from csv import writer,reader
from typing import List
from funcoes import verifica_email,verifica_nome,verifica_telefone,NOME,EMAIL,TELEFONE


def menu_macro():
    '''
    Função exibe um menu inicial em que o usuário deverá digitar um número para realizar uma ação
    '''
    print('''
        
        ####################################################### 
        #################### PyCoders Ltda ####################
        #######################################################
        
        Digite sua escolha:

        1 - Para adicionar fornecedores
        2 - Para deletar fornecedores
        3 - Para buscar fornecedores
        4 - Para exibir os fornecedores cadastrados
        5 - Para salvar
        Digite qualquer outra técla ou aperte enter para sair

        ''')
    return input(">")

def add(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas organizada e receberá inputs do usuário de nome,telefone e email para serem adicionados na lista
    '''

    print('''
    
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$ Adição de fornecedor $$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    ''')
    
    print("        Deseja prosseguir com a adição do fornecedor? [s/n]") #espaço somente para alinhar com o print acima
    print("        Digite qualquer outra técla para retornar ao menu inicial")
    escolha_add = input(">")
    while True:    
        if escolha_add.lower() == "s":
            nome = input("        Digite o nome do fornecedor: ")
            telefone = input("        Digite o telefone do fornecedor (só números): ")
            email = input("        Digite o e-mail do fornecedor (e-mails válidos): ")

            if all([verifica_nome(nome),verifica_telefone(telefone),verifica_email(email)]):
                print("        Fornecedor cadastrado com os dados:")
                print(f"        Nome: {nome}")
                print(f"        Telefone: {telefone}")
                print(f"        E-mail: {email}")
                lista[NOME].append(nome)
                lista[EMAIL].append(email)
                lista[TELEFONE].append(telefone)
                add(lista)
                break
            print("Ops!Dados inválidos!")
        break
    

def deleta(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas com os clientes, receberá um nome de um cliente e buscará esse nome, deletando-o depois, caso seja encontrado
    '''
    
    print('''
    
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$ Remoção de fornecedor $$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    ''')
    print("        Deseja prosseguir com a remoção de fornecedor? [s/n]")
    print("        Digite qualquer outra técla para retornar ao menu inicial")
    escolha_deleta = input(">")
    if escolha_deleta.lower() == "s":
        nome = input("        Digite o nome do fornecedor que deseja deletar: ")
        if nome not in lista[NOME]:
            print("        Ops. Cadastro a ser deletado não foi encontrado")
        else:
            index = lista[NOME].index(nome)
            deletado = [lista[i].pop(index) for i in range(3)]
            print("        O fornecedor com os seguintes dados foi deletado")
            print(f"        {deletado}")
        deleta(lista)

def busca(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas com os dados de nome, email e telefone dos clientes. Recebe um input do usuário de nome, email ou telefone para pesquisa e chama as funções de busca por nome, email e telefone
    '''
    print('''
    
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$ Busca de fornecedor $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
        Selecionar se quer buscar por:
        1 - Nome
        2 - Telefone
        3 - E-mail
        Para sair digite qualquer técla ou aperte enter
    ''')
    escolha_busca = input(">")

    while True:
        if escolha_busca == "1":
            busca_nome(lista)
            busca(lista)
        elif escolha_busca == "2":
            busca_telefone(lista)
            busca(lista)
        elif escolha_busca == "3":
            busca_email(lista)
            busca(lista)
        break

def busca_nome(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas com os dados dos clientes, o usuário digita um input de nome e será chamada uma função para buscar se esse nome existe em uma das listas de listas recebidas
    '''
    print('''
        
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$ Pesquisa de fornecedor por NOME $$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            
        Digite o nome do fornecedor que você quer pesquisar:
        ''')
    nome = input("        >: ")
    indices(lista,nome,0)
    


def busca_telefone(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas com os dados dos clientes, o usuário digita um input de telefone e será chamada uma função para buscar se esse telefone existe em uma das listas de listas recebidas
    '''
    print('''
        
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$ Pesquisa de fornecedor por TELEFONE $$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            
        Digite o telefone do fornecedor que você quer pesquisar:
        ''')
    telefone = input("        >: ")
    indices(lista,telefone,1)
  

def busca_email(lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas com os dados dos clientes, o usuário digita um input de email e será chamada uma função para buscar se esse email existe em uma das listas de listas recebidas
    '''
    print('''
        
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$ Pesquisa de fornecedor por E-MAIL $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            
        Digite o telefone do fornecedor que você quer pesquisar:
        ''')
    email = input("        >: ")
    indices(lista,email,2)
    

def indices(lista:List[List[str]],campo:str,n_campo:int)->None:
    '''
    Função recebe uma lista de listas com os dados do cliente, um campo a ser buscado nas listas e o numero que servirá como índice da lista de listas. Por exemplo, se o número do campo for 1 ele buscará na primeira lista da lista de listas
    A partir dai ele buscará se esse campo existe na lista que corresponde ao número do campo. 
    Caso ele exista será salvo o indice do campo para ser possível imprimir os dados do cliente. 
    '''    
    indices = []
    contador = 0
    for campos in lista[n_campo]:
        if campo in lista[n_campo][contador]:
            indices.append(contador)
        contador +=1
    if len(indices) > 0:
        for i in indices:
            print(8*" ",[lista[NOME][i],lista[TELEFONE][i],lista[EMAIL][i]])
    else:
        print("        Fornecedor não encontrado")

 
def salva_lista(lista:List[List[str]])->None:
    '''
    Função que recebe uma lista de listas com uma lista para cada cliente com (nome, telefone e email) e escreverá essas linhas em um novo arquivo CSV
    '''
    print("        Digite o nome que quer no arquivo salvo. Se não aperte enter e será salvo como \'contatos_organizado.csv\'")
    nome_arquivo = input(">")
    if nome_arquivo == '':
        nome_arquivo = 'contatos_organizado.csv'
    with open(nome_arquivo,"w",encoding='utf-8') as arquivo_out:
        writer(arquivo_out,delimiter=";",lineterminator="\n").writerows(padrao_lista_csv(lista))
    print(f"        Arquivo salvo com o nome \'{nome_arquivo}\'")

def ordena_lista(lista:List[List[str]])->None:
    '''
    Função recebe uma lista com com os campos nome,número e telefone desordenados, le essa lista e chamará uma função que ordena esses campos em uma nova lista com as "colunas" corretas
    '''
    with open("contatos.csv","r",encoding="utf-8") as arquivo_inicial:
        arquivo_inicial = reader(arquivo_inicial,delimiter=";",lineterminator="\n")
        for line in arquivo_inicial:
            for item in line:
                ordena_item(item,lista)

def ordena_item(item:str,lista:List[List[str]])->None:
    '''
    Função recebe uma lista de listas vazias e um item de um lista de listas "desorganizada". Ela pegará esse item e verificará se ele é um nome,email ou telefone e o adicionará na lista vazia em uma das listas
    '''
    if verifica_email(item):
        lista[EMAIL].append(item)
    elif verifica_telefone(item):
        lista[TELEFONE].append(item)
    elif verifica_nome(item):
        lista[NOME].append(item)

def padrao_lista_csv(lista:List[List[str]])->List[List[str]]:
    '''
    Função recebe uma lista com 3 colunas e cada coluna com um numero x de elementos. Transforma essa lista de listas em x listas com 3 elementos cada
    '''
    lista_out = [[lista[NOME][i],lista[TELEFONE][i],lista[EMAIL][i]] for i in range(len(lista[NOME]))]
    return lista_out

def main():
    '''
    Função mãe do programa que o inicializa
    '''

    lista = [[],[],[]]
    ordena_lista(lista)
    escolha = menu_macro()
    
    while True:
        if escolha == '1':
            add(lista)
            escolha = menu_macro()
        elif escolha == '2':
            deleta(lista)
            escolha = menu_macro()
        elif escolha == '3':
            busca(lista)
            escolha = menu_macro()
        elif escolha == '4':
            for cadastro in padrao_lista_csv(lista):
                print(f"        {cadastro}")
            escolha = menu_macro()
        elif escolha == '5':
            salva_lista(lista)
            escolha = menu_macro()
        else:
            break
        

main()