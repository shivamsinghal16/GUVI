n = int(input("Enter a no.: "))

x = 0
y = n

while(n!=0):
    r = n%10
    n //= 10
    x = (x*10) + r

if x == y:
    print("yes")
else:
    print("no")
