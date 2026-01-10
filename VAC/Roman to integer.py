class Solution(object):
 def romanToInt(self, s):
   rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
   result = 0
   for i in range(len(s)):
     cval = rom[s[i]] #s[0] = X #cval = 10
     nval = rom[s[i+1]] if i+1 < len(s) else 0
     if cval >= nval:
       result = result + cval
     else:
       result = result - cval
   return result
