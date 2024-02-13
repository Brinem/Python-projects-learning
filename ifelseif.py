# Else if statement
marks = int(input("Enter Marks Scored"))

if 80 <= marks <= 100:
    print("You have Scored a A")
elif 60 <= marks <= 79:
    print("You have Scored a B")
elif 40 <= marks <= 59:
    print("You have Scored a C")
elif 0 <= marks <= 39:
    print("You have Scored a E")
else:
    print("Invalid Marks Value")
