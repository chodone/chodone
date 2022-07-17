



from curses.ascii import isupper


def unComp(alp,num ,n):
    if isupper(alp) and 1 <= num <= 20:
        doc[alp] = num
        
    



testCase = int(input())

doc = {}

for i in range(testCase):
    n = int(input())
    for i in range(n):
        alp , num = map(str, input().split())
        num = int(num)
        unComp(alp, num , n)
        
    
