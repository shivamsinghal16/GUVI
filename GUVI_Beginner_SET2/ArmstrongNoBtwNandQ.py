n,q = map(int, input().split())

for i in range(n+1,q):
    l = len(str(i))
    Sum = 0
    y = i

    while(y!=0):
        r = y%10
        y //= 10
        Sum += (r**l)

    if Sum == i:
        print(i, end=' ')
