class Solution(object):
 def thirdMax(self, nums):
   a = list(set(nums))
   a.sort(reverse=True)
   if len(a) >= 3:
     return a[2]
   else:
     return a[0]
