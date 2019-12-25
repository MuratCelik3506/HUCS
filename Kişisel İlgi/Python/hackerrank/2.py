N,M,X,Y = input().split()
N = int(N)
M = int(M)
X = int(X)
Y = int(Y)

e = M //X
b= M % X
c = N - e
c = c - e
i=0
d = b
while c>0:
    c-=1
    d = 1*Y + d
    if d >=X and c>0:
        c-=1
        d=d-X
        e+=1
print(e)
