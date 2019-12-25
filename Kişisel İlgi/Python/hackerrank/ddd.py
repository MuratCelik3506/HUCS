a=list(input())
for x in range(0, len(a),2):
    a[x] = int(a[x])
N = a[0]
C = a[2]
X1 = a[4]
U = a[6]
X2 = a[8]
i=0
K=0
while i <N:
    if i ==0:
        C = C + X1
    if C >=U:
        K= K + 1
        C = C - U
    sum=X1+X2*K
    C = C + sum
    i = i + 1
print(C)

