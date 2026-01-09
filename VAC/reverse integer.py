def revint(x):
 sign = -1 if x<0 else 1
 x = abs(x)
 res = 0
 while x!=0:
   dig = x%10
   res = res*10 + dig
   x = x//10
 res = res*sign
 if res in range(-2**32,2**32-1):
   return res
 else:
   return 0
