#Constantes que serão usadas para definir o numero da lista de uma lista de listas
NOME = 0
TELEFONE = 1
EMAIL = 2

def verifica_email(item:str)->bool:
    '''
    Recebe uma string e verificar se ela é um e-mail, ou seja, caso contenha arroba
    '''
    return "@" in item

def verifica_telefone(item:str)->bool:
    '''
    Recebe uma string e verificar se ela só tem digitos, ou seja, é um telefone
    '''
    return item.isdigit()

def verifica_nome(item:str)->bool:
    '''
    Recebe uma string e verificar se ela é um nome diferente de vazio
    '''
    return item.strip() and item !=""