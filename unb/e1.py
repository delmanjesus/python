def lista(s1,s2):
    l1 = s1.split()
    
    l2 = s2.split()
    x = int(l2[0])
    y = int(l2[1])
    
    return l1[x:y]

s1 = '0 1 2 3 4 5 6 7'
s2 = '2 5'
res = lista(s1,s2)
print(res)