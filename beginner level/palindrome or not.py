a=input('enter the string')
b=''.join(reversed(a))
if a==b:
  print("is a palindrome")
  print('yes')
else:
  print("is not a palindrome")
  print('no')
