s = 'delma jesus'

res= s.replace('d','D') # .replace() substitui algo.
print(res)

res= s.upper() #.upper troca para maiuscula
print(res)

res= s.upper().lower() #.apos deixar tudo maiusculo, coloquei tudo minusculo porque o lower vem em seguida. e ele ultiliza o ultimo. 
print(res)

res= s.title() #
print(res)

res= s.split()
print(res)

res= s[0]+s[-1]
print(res)

res= s[2:7]
print(res)

s = 'delma,jesus'

res= s.split(',')
print(res)

s = '    delma     jesus   '
res= s.strip()
print(res)

