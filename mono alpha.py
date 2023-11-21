import random
p=[]
w=[]
def encrypt(a):
    s = list(a)
    random.shuffle(s)
    return ''.join(s)
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    p.append(i)
x=encrypt(a)
for i in x:
    w.append(i)
n = str(input("Eter text: "))
z = ''
for i in n:
    for j in range(26):
        if i ==p[j]:
            z += w[j]
print(z,end='')
            

