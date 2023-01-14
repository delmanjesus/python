"""
este codigo demonstra como se utiliza a operação  math de modulo no python. 
o modulo "%" verifica o resto da divisão. 
"""
def valor_par(numero):
    """
    esta função usa a operacao de modulo para verificar se um valor é impar ou par. 
    INPUT:
    numero(int): valor que sera analisado. 
    RETURN:
    (bool): Se retornar True é par, se retornar False é impar. 
    """
    numero= int(numero)
    if numero%2==0: #se o modulo de 2 for igual a zero é porque é par. 
        return True
    if not numero%2==0: #como estamos usando o not faz a operação inversa. 
        return False


numero = int(input('insira um numero:')) #pegando o valor do usuario e transformando em um int para jogar no codigo.  
res = valor_par(numero)

if res == True: 
    print("É par!")
else:
    print("É impar!")


