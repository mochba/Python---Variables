"""Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program 
(the pay should be 96.25). You should use input to read a string and float() to 
convert the string to a number. 

1.Use try and except handles non-numeric input gracefully by printing a message and 
exiting the program.

2.And pay computation to give the employee 1.5 times the hourly rate for hours worked above 
40 hours."""

Hours  = input("Enter number of hours worked :")
Rate   = input("Enter a rate per hour :")
try:
    if Hours.isdigit() and Rate.isdigit():
        Hours = float(Hours)
        Rate  = float(Rate)
        if Hours >= 40:
            OverTime = Hours - 40
            Regular_Hour = Hours - OverTime
            Grosspay = (OverTime * 1.5 * Rate ) + (Regular_Hour *Rate)
        else:
            Grosspay = Rate * Hours
    print("Gross Pay :" , Grosspay)
except:
    print("Error, please enter numeric input")