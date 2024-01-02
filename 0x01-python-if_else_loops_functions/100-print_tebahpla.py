#!/usr/bin/python3
b = False
for i in range(122, 96, -1):
	if b == True:
		print("{}".format(chr(i - 32)), end="")
		b = False
	else:
		print("{}".format(chr(i)), end="")
		b = True
