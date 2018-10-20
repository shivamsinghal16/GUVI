n = int(input("Enter the total no. of elements: "))
arr = list(map(int,input().split()))

arr.sort()

if len(arr) != n:
    print("Invalid Array Length")
else:
    print(*arr)
