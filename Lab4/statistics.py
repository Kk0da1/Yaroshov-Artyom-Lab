q=0
w=0
e=-1000000
for i in range(int(input())):
    b=int(input())
    if b>0:
        q+=1
        w+=b
        e=max(e,b)
print(q, w, e)
