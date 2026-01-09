def findCount(arr,length,num,diff):
  count=0
  for i in arr:
    if abs(i-num)<=diff:
      count+=1
  return count
