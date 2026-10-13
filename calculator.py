while True:
 try:
  num1=float(input("Enter the first number: "))
  num2=float(input("Enter the second number: "))
 except ValueError:
   print("Please enter valid number")
   break

 print("\nChoose and operation")
 print("1.Addition(+)")
 print("2.Subtraction(-)")
 print("3.Multiplication(*)")
 print("4.Division(/)")


 operation=input("\nChoose an operation(1/2/3/4):")

 if operation == "1":
   result = num1 + num2
   print("Result:",result)
 elif operation == "2" :
   result = num1 - num2
   print("Result:",result)
 elif operation == "3" :
   result = num1*num2
   print("Result:",result)
 elif operation == "4" :
  if num2 !="0":
   result = num1/num2
   print("Result:",result)
  else:
    print("The number cannot be divided by zero")
 else:
   print("Invalid operation")

 again = input("Calculate again? (yes/no):")

 if again !="yes":
   print("Thank you for using the calculator")
   break

