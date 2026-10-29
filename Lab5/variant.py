q=input('Текст:')
q=q.split()
for i in q:
    i=i.strip(".,!?;:").lower()
    if i[0]==i[-1]:
        print(i)
