n = int(input("Enter the total no. of elements: "))
arr = list(map(int,input().split()))

arr.sort()

if len(arr) != n:
    print("Invalid Array Length")
elif len(arr)%2 != 0:
    print(arr[len(arr)//2])
else:
    median = (arr[len(arr)//2-1] + arr[len(arr)//2]) / 2
    print(median)
