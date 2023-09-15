num=int(input("Enter a number: "))
if num<0:
  print("Sorry, factorial does not exist for negative numbers")
elif num==0:
  print ("the factorial of 0 is 1")
else:
  print("the factorial of",num,"is",recur_factorial(num))