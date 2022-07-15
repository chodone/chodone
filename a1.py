# 1936 가위 바위 보

n1, n2 = map(int , input().split())

if n1 == 1 and n2 == 3:
    print("A")
elif n1 == 2 and n2 == 1:
    print("A")
elif n1 == 3 and n2 == 2:
    print("A")
else:
    print("B")
