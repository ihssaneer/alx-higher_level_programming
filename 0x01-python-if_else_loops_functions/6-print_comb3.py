#!/usr/bin/python3
i = 0
for i in range(9):
	for j in range(i + 1, 10):
		if i == 8:
			print("{}{}".format(i, j))
			break
		print("{}{}, ".format(i, j), end="")
