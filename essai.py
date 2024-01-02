#! /usr/bin/python3
der = input("which direction you wants to count (up or down): ")
#num2 = int(input("Enter num 2:"))
if der == "up":
    num = int(input("Entre the top number : "))
    for i in range(1, num):
        print(i, " ", end="")
elif der == "down":
    num = int(input("Entre a number below 20 : "))
    for i in range(20, num - 1, -1):
        print(i, " ", end="")
else:
    print("I don’t understand.")
print()