
def rec(n): 
    """ 
    função de recursão. 
    INPUT: 
    n(int): valor de entrada utilizado para o calculo e que será jogado no if. 
    RETURN:
    está função não tem retorno, ela apenas usa o print. 
    Por isso, não é necessario ao chamar a função salvar o valor em uma variavel. 

    """
    if n>= 0:
        print(n)
        rec(n -1) #ele chama a funcao novamente, mas decrementado o valor, a função so ira parar de ser chamada quando o If não for atendido.  

rec(4) # o numero 4 é o paramentro de entrada, mas o n poderia ter sido definido antes.
 