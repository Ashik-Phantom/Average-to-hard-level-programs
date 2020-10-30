# Sort Books - Published Year
"""
The program must accept the name and the published year of N books as the input. The program must print the name and the published year of the books based on the following conditions as the output.- The books must be sorted in descending order based on the published year.- If two or more books have the same published year, then those books must be sorted in ascending order based on the book name.- If a book with multiple editions (i.e., A book has published more than once), then consider only the most recently published book.Boundary Condition(s):1 <= N <= 501 <= Length of the name of each book <= 201800 <= Published year of each book <= 2020Input Format:The first line contains N.The next N lines, each contains the name and the published year of a book separated by a space.Output Format:The line(s), each contains the name and the published year of a book separated by a space.Example Input/Output 1:Input:6Abc 2001XYZ 1997pqr 2002Abc 2010Abc 2006Efg 2002Output:Abc 2010Efg 2002pqr 2002XYZ 1997Explanation:The book Abc has three editions. The first edition was published in 2001, the second edition was published in 2006 and the third edition was published in 2010. So the most recently published book (Abc 2010) is considered.The book XYZ was published in 1997.The book pqr was published in 2002.The book Efg was published in 2002.After sorting the books based on the given conditions, the books becomeAbc 2010Efg 2002pqr 2002XYZ 1997Example Input/Output 2:Input:5IJK 1996IJK 2011IJK 2006pqr 2010IJK 2010Output:IJK 2011pqr 2010
"""

# Solution 

n=int(input())
book=[]
for i in range(n): 
    a,b=input().split() 
    book.append([a,b]) 
book=sorted(book,key=lambda x:x[0]) 
book=sorted(book,key=lambda x:x[1],reverse=1)
books=[]
year=[] 
for i in range(n): 
    if book[i][0] not in books: 
        year.append(book[i]) 
        books.append(book[i][0]) 
for i in year: 
    print(*i)
