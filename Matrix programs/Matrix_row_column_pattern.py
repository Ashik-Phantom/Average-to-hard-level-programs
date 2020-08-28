# Matrix Row - column pattern

n,m=map(int,input().split()) 
l=[list(map(int,input().split())) for i in range(n)] 
while l: 
    print(*l[0]) 
    l=l[1:] 
    l=[list(i) for i in zip(*l)]
