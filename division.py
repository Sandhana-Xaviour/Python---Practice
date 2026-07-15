num1 = float (input ("Enter the first number :"))
num2 = float (input ("Enter the second number :"))

if num2 == 0:
    print ("Zero division error")
else:
    division_result = num1 / num2
    print (f" The divsion of {num1} and {num2} is {division_result}")