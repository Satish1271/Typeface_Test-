valid=['0','1','2','5','6','8','9']
n=int(input())
num=1
while n>0:
    l=list(str(num))
    if(set(l).issubset(valid)):
        n-=1
    num+=1
print(num-1)
