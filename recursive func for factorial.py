def rec_facto(n):
  if n==1:
    return 1
  else:
    return n*rec_facto(n-1)
n=int(input('Enter the number: '))
print(rec_facto(n))