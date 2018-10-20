n = int(input("Enter a no.: "))
l = len(str(n))

Sum = 0
y = n

while(y!=0):
    r = y%10
    y //= 10
    Sum += (r**l)

if Sum == n:
    print("yes")
else:
    print("no")
