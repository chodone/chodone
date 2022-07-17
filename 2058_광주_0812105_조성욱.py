n = int(input())

if 1 <= n <= 9999:
    first = n // 1000
    n = n - first*1000
    second = n // 100
    n = n - second*100
    third = n // 10
    fourth = n - third*10

    sum = first + second + third + fourth

    print(sum)