print ("Simple Calculator")

num1 = float(input("Enter First Number  Here: "))
num2 = float(input("Enter Second Number Here:"))

print("Choose Operation:")
print("Press 1 for Addition (+)")
print("Press 2 for Subtraction(-) ")
print("Press 3 for Multiplication(*)")
print("Press 4 for Division(/)")

Choice= int(input("Enter your Choice form 1-4:"))

if Choice == 1 :
    print("The addition of given two numbers  is", num1 + num2)
elif Choice == 2 :
    print("The subtraction of given two numbers is " ,num1 - num2)
elif Choice == 3 :
    print("The multiplication of given two numbers is  " , num1 * num2)
elif Choice == 4:
    print("The division of  given two numbers is ", num1 / num2)

else:
    print("Invalid Input") 