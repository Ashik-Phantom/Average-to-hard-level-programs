"""
Find All Sundays in a Month
The program must accept two string values S1, S2 and an integer Y as the input. 
The string S1 represents the weekday of the 1st Jan in the year Y. The string S2 represents a month in the year Y. 
The program must print the dates of all the sundays in the month S2 of the given year Y as the output. 
Each date must be printed in the format DD-MMM-YYYY.Note:
-The value of the weekday S1 will be from Sun, Mon, Tue, Wed,... till Sat.
- The value of the month S2 will be from Jan, Feb, Mar, Apr,... till Dec.
Input Format:
The first line contains S1.
The second line contains S2.
The third line contains Y.
Output Format:
The lines contain the dates of all the sundays in the month S2 of the given year Y.

Example Input/Output 1:
Input:
Fri
May
2021
Output:
02-May-2021
09-May-2021
16-May-2021
23-May-2021
30-May-2021
Explanation:
Here S1 = Fri, S2 = May and Y = 2021.
The dates of all the sundays in May-2021 are given above

Example Input/Output 2:
Input:
Sun
Aug
1984
Output:
05-Aug-1984
12-Aug-1984
19-Aug-1984
26-Aug-1984
"""

#Solution 

s1=input().strip()
s2=input().strip()
year=int(input())
weekdays=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
mon=[31,28,31,30,31,30,31,31,30,31,30,31]
if(year%400==0 or (year%4==0 and year%100!=0)):
    mon[1]+=1 
m=months.index(s2)
x=weekdays.index(s1)
for i in range(m):
    x+=mon[i]
x=x%7
for i in range(1,mon[m]+1):
    if(x%7==0):
        print("%02d-%s-%d"%(i,s2,year))
    x+=1
    
    
#using calender 

import calendar
s1=input().strip()
s2=input().strip()
y=int(input())
mon=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month=calendar.monthcalendar(y,mon.index(s2)+1)
la=max(month[-1][calendar.SUNDAY],month[-2][calendar.SUNDAY])
fi=min(month[0][calendar.SUNDAY],month[1][calendar.SUNDAY])
for i in range(fi,la+1,7):
    print("%02d"%(i),end="")
    print("-"+s2+"-"+str(y))
    
    
#using date time 

from datetime import datetime as dt
from datetime import timedelta as td
S1, S2, Y = input().strip(), input().strip(), int(input())
S = dt.strptime("{}-{}-01".format(Y, S2), "%Y-%b-%d")
month = S.month
while S.month == month:
    if(dt.strftime(S, "%A") == "Sunday"): print(dt.strftime(S, "%d-%b-%Y"))
    S+=td(days=1)
    
