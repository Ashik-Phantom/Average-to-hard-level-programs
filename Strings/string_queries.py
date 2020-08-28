#String -Queries

s = input().strip()
n = int(input()) 
for i in range(n):
    S=input().strip() 
    x,y=S.split('+') 
    if y.isdigit():
        s=s+s[-int(y):]
    else:
        s=s[:int(x)]+s
print(s)    
