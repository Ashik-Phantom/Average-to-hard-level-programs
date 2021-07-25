def isleap(x): 
    if x%4==0: 
        if x%100==0: 
            if x%400==0: 
                return 1 
            else: 
                return 0 
        else: 
            return 1 
    else: 
        return 0 
def checkrange(x): 
    if len(x)==1: 
        return '0'+x 
    return x
m,n=map(int,input().split()) 
y=int(input())
days=[]
if y>=1000: yy=str(y)
elif y>=100: yy='0'+str(y)
elif y>=10: yy='00'+str(y)
else: yy='000'+str(y)
    
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Jan'+'-'+yy)
if isleap(y)==0: 
    for j in range(1,29): days.append(checkrange(str(j))+'-'+'Feb'+'-'+yy)
else: 
    for j in range(1,30): days.append(checkrange(str(j))+'-'+'Feb'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Mar'+'-'+yy)
for j in range(1,31): days.append(checkrange(str(j))+'-'+'Apr'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'May'+'-'+yy)
for j in range(1,31): days.append(checkrange(str(j))+'-'+'Jun'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Jul'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Aug'+'-'+yy)
for j in range(1,31): days.append(checkrange(str(j))+'-'+'Sep'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Oct'+'-'+yy)
for j in range(1,31): days.append(checkrange(str(j))+'-'+'Nov'+'-'+yy)
for j in range(1,32): days.append(checkrange(str(j))+'-'+'Dec'+'-'+yy)
    
citya,cityb=[],[] 
a=0
while(1): 
    try: 
        citya.append(days[a]+' to '+days[a+m-1]) 
        a+=m 
    except: 
        f=0 
        break 
    try: 
        cityb.append(days[a]+' to '+days[a+n-1])
        a+=n 
    except: 
        f=1 
        break
if f==0: 
    try: 
        citya.append(days[a]+' to '+days[-1])
    except: pass
elif f==1: 
    try: 
        cityb.append(days[a]+' to '+days[-1])
    except: 
        pass
print('City A:')
for i in citya:
    print(i)
print('City B:')
for i in cityb: 
    print(i)
"""
input:
30 30
2021
"""
