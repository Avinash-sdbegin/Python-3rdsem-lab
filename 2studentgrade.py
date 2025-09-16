marks = int(input("Enter your marks: "))

if marks >= 90:
    print("The grade achieved is : A")
elif marks >= 80 and marks < 90:
    print("The grade achieved is : B")
elif marks >= 70 and marks < 80:
    print("The grade achieved is : C")
elif marks >= 60 and marks < 70:
    print("The grade achieved is : D")
else:
    print("The grade achieved is : E")
