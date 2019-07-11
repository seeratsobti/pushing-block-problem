while(True):
	print("Enter M, P, F: \n")
	stack = list(map(int, input().split()))
	M = stack[0]
	P = stack[1]
	F = stack[2]

	if(P == 0 and M == 0 and F == 0):
		break
	else:
		rowList = []

		for i in range(M):
			row = list(map(int, input().split()))
			rowList.append(row)

		for i in range(M):
			print(rowList[i])

		f_input = list(map(int, input().split()))
		k = 0

		j = P-1
		def Block():
			global j, k
			if(j >= 0):
				for i in range(M-1, -1, -1):
					if(rowList[i][j] == 0 and k < F):
						rowList[i][j] = f_input[k]
						k += 1
				j -= 1
				Block()

		Block()
		for i in range(M):
			print(rowList[i])