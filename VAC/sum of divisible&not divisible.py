def dd(limit,n):
  sd=0
  snd=0
  for i in range(1,limit+1):
    if i%n==0:
      sd+=i
    else:
      snd+=i
  return abs(sd-snd)
