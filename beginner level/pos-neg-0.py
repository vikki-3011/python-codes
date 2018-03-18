ch = str(input("Enter any character: "));
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
  print("the given no is invalid")
else:
  b=int(ch)
  if(b>0):
    print("\n input is postive")
  elif(b==0):
    print("\n the input value is zero")
  else:
    print("\n the input value is negative")
