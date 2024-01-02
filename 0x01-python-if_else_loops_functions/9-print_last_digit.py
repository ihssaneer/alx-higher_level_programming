#!/usr/bin/python3
def print_last_digit(number):
	ldigit = 1
	if number < 0:
		number *= -1
		ldigit = number % 10
	else:
		ldigit = number % 10
	print("{}".format(ldigit), end="")
	return ldigit
