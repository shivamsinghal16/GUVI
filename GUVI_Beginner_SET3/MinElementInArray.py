n = int(input("Enter the total no. of elements: "))
arr = list(map(int,input().split()))

if len(arr) != n:
    print("Invalid Array Length")
else:
    print(min(arr))
