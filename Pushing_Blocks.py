print("Enter M, P, F: \n")
stack = list(map(int, input().split()))
M = stack[0]
P = stack[1]
F = stack[2]

rowList = []

for i in range(M):
	row = list(map(int, input().split()))
	rowList.append(row)

# colList = []
# for i in range(P):

# 	colList.append()


for i in range(M):
	print(rowList[i])

# print(rowList[3][4])

f_input = list(map(int, input().split()))
k = 0

for j in range(P-1, -1, -1):
	for i in range(M-1, -1, -1):
		# print('i: {}, j: {}'.format(i, j))
		# print(rowList[i][j])
		if(rowList[i][j] == 0 and k < F):
			# print('i: {}, j: {}'.format(i, j))
			rowList[i][j] = f_input[k]
			k += 1
		# else:
		# 	break

for i in range(M):
	print(rowList[i])