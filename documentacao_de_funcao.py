def saudacao(nome):
    """
    esta funcao faz uma saudaacao.
    INPUT: 
    nome(str): nome da pessoal que sera saudado. 
    RETURN: 
    msg(str): mensagem de saaudacao
    """
    msg = f'Bem-vindo,{nome}!'
    return msg 


nome = 'Rob'

res = saudacao(nome)
print(res)