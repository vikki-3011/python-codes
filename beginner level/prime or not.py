n=int(input("enter the value"))
c=0
for i in range(1,n):
  if(n%i==0):
    c=c+1
    if(c==2):
      print("not prime")
    else:
      print("prime")
