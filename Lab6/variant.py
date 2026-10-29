a=[int(input()) for i in range(int(input()))]
print(a)
a.sort()
k=0
sm=0
for i in a:
    if i>=10:
        k+=1
        sm+=i
print(a, k, sm)