def Checkpassword(char,n):
  if n<4: #0,1,2,3
    print("Invalid because of less length!")
    return 0
  if char[0]>='0' and char[0]<='9':
    print("Invalid because starts with number")
    return 0
  nf=0
  capf=0
  spe=0
  for i in char:
    if i>='0' and i<='9':
      nf=1
    elif i>='A' and i<='Z':
      capf=1
    elif i==" " or i=="/":
      spe=1
print("Number flag:",nf)
print("capital flag:",capf)
print("Special flag:",spe)
if nf==1 and capf==1 and spe==0:
  return 1
else:
  return 0
