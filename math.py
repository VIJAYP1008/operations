try:
  a=float(input("enter first number :"))
  b=float(input("enter second number:"))
  print(f"addition:{a+b}")
  print(f"substraction:{a-b}")
except valueError:
  print("please enter valid number .")
