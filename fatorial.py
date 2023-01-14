#funcao fatorial
#fatorial de 4: !4= 4.3.2.1 

def funcao_fatorial(n):

    """
    esta funcao reproduz uma operacao de fatorial.
    Ela usa uma recursao, recursao é quando uma funcao chama a ela mesma. 
    INPUT:
    n(int): é o valor que sera fatorado. 
    RETURN: 
    """
    if n == 0:
        return 1
    else:
        #nesse caso o valor sera decrementado e a funcao sera chamada novamente ate que a condicao do if seja atendida. 

        return n*funcao_fatorial(n-1)

#para chamar uma funcao, coloque o nome dela com parenteses após e se necessario coloque os paramentros de entrda dentro. 
# ex: funcao_fatorial(paramentro)


resultado = funcao_fatorial(5) #salvando o retorno da funcao na variavel resultado

print(resultado) #printando resultaddo para o usuario visualizar. 
