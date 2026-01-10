arr=[2,6,1,7,8]
limit=int(input())
arr.sort()
s=arr[0]+arr[1]
if s<=limit:
print(arr[0]*arr[1])
else:
print(0)
