nomes = """Alexandre da Silva
Ana Roberta
Leandro Beloti
Zara Araújo"""

def x(nomes,n=len(nomes.split('\n'))):
    print(n)
    if n>0:
        return sorted(nomes.split('\n'), reverse=True)
    else: 
        return ''


r =x(nomes); print(r)

