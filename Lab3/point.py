q=int(input())
w=int(input())
if (q<5 and q>0) and (w>0 and w<3):
    print('Внутри прямоугол')
elif ((q==5 or q==0) and 0<=w<=3) or ((w==0 or w==3) and 0<=q<=5):
    print('На границе')
elif (q>0 or q>5) or (w<0 or w>3):
    print('За границей')
