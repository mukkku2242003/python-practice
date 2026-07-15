try:
   num1=int(input("enter your first number"))
   num2=int(input("enter your second number"))
   x=num1 / num2
   print(x)
except ZeroDivisionError:
   print("zero is not divisable any number ") 
   