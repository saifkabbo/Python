try:
    num = float(input("Enter a number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Division Successful.")

finally:
    print("Program Finished.")