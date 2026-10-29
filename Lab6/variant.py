q=[int(input()) for i in range(int(input()))]
print(q)
q.sort()
w=0
sm=0
for i in q:
    if i>=10:
        w+=1
        sm+=i
print(q, w, sm)
