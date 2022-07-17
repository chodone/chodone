# 2063 중간값 찾기

n = int(input())


if 9 <= n <= 199 and n % 2 == 1: 
    
    numList = list(map(int, input().split()))
    numList.sort()


    print(numList[n//2 ])
