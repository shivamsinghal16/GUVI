n = int(input("Enter a no.: "))

flag = 0

for i in range(2,(n//2)+1):
    if n%i == 0:
        print("no")
        flag = 1
        break

if flag == 0:
    print("yes")
