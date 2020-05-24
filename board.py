def displayBoard(board):
	seperateLine = "=" * 55
	horizonLine = "X-----+-----+-----" * 3 + "X"
	verticalLine = "|" + "     |" * 9

	print(seperateLine)
	print("Wlecome to Yoki's Sudoku".center(48))
	for rows in board:
		print(horizonLine)
		print(verticalLine)
		dataLine =""
		# Use iterate 9 elements of each row
		for item in rows:
			# concadenate all the data
			dataLine += "|  " + item + "  "
		else:
			dataLine += "|"
			# print the data after the itaration
			print(dataLine)

		print(verticalLine)
	else:
		print(horizonLine)
		print(seperateLine)
