"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of 
range, print an error message. If the score is between 0.0 and 1.0, print a grade 
using the following table: 
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F """
try:
    score = float(input("Enter a score between 0.0 and 1.0 :"))
    if score >= 0.9 and score <= 1.0: 
        print("Grade A")
    elif score >= 0.8 and score <= 1.0:
        print("Grade B")
    elif score >= 0.7 and score <= 1.0:
        print("Grade C")
    elif score >= 0.6 and score <= 1.0:
        print("Grade D")
    elif score < 0.6 and score >= 0.0:
        print("Grade F")
except:
    print("Please, Enter a number between 0.0 and 1.0")