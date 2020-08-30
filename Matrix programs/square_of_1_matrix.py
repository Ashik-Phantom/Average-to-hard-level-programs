def finish(): 
    for i in l: 
        print(*i) 
        exit()
        
r,c = map(int,input().split())
l = []
for i in range(r): 
    k = list(map(str,input().split())) 
    if 'X' in k: 
        posi = i 
        posj = k.index('X') 
    l.append(k)
f = 0 
postempi = posi
postempj = posj 
sizei = posi+2 
sizej = posj+2
res=[]
while(f == 0): 
    if posi <= 0 or posj <= 0 or sizei > r or sizej > c:
        finish() 
    for i in range(posi-1, sizei): 
        for j in range(posj-1, sizej): 
            res.append(l[i][j]) 
    if '0' not in res: 
        res = [] 
        posi -= 1 
        posj -= 1 
        sizei += 1 
        sizej += 1 
    else: 
        for i in range(posi-1, sizei): 
            for j in range(posj-1, sizej): 
                if i == postempi and j == postempj: 
                    l[i][j] = 'X' 
                else: 
                    l[i][j] = '1' 
        finish()
