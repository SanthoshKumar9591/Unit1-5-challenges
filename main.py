n= int(input("Enter input number : "))
 
fact = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
  while(n > 0):
        fact = fact * n
        n = n - 1
  print("The factorial is",fact)