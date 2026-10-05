q=int(input())
w=int(input())
if q>w:
    for i in range(q, w-1,-1):
        print(i)
else:
    for i in range(q, w+1):
        print(i)
