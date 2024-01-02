#!/usr/bin/python3
"""def print_0_to_99_rec(num = 0):
	if num < 99:
		print("{:02d}, ".format(num), end="")
		print_0_to_99_rec(num + 1)
	if num == 99:
		print("{}".format(num))
print_0_to_99_rec()"""
for num in range(100):
	if num == 99:
		print("{:02d}".format(num))
		break   
	print("{:02d}, ".format(num), end="")
