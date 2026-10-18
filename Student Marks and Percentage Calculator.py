

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
computer = float(input("Enter Computer marks: "))


total = maths + physics + computer
percentage = total / 3


print("Total marks:", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
else:
    print("Grade: C")
