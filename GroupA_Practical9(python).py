row=int(input("Enter no. of rows : "))
col=int(input("Enter no. of columns : "))

A_mat=[[0 for j in range(col)]for i in range(row)]

for i in range(row):
	for j in range(col):
		item=int(input("Enter elements : "))
		A_mat[i][j]=item

print("First matrix is : ")

for n in A_mat:
	print(n)

B_mat=[[0 for j in range(col)]for i in range(row)]

for i in range(row):
	for j in range(col):
		item=int(input("Enter elements : "))
		B_mat[i][j]=item

print("Second matrix is : ")

for n in B_mat:
	print(n)

C_mat=[[0 for j in range(col)]for i in range(row)]
def add_matrix(A_mat,B_mat,row,col):
	for i in range(row):
		for j in range(col):
			C_mat[i][j] = A_mat[i][j] + B_mat[i][j]
	print("Addition of two matrices : ")
	for n in C_mat:
		print(n)

def sub_matrix(A_mat,B_mat,row,col):
	C_mat=[[0 for j in range(col)]for i in range(row)]
	for i in range(0,row):
		for j in range(0,col):
			C_mat[i][j] = A_mat[i][j] - B_mat[i][j]
	print("Subtraction of two matrices : ")
	for n in C_mat:
		print(n)

def mul_matrix(A_mat,B_mat,row,col):
	C_mat=[[0 for j in range(col)]for i in range(row)]
	for i in range(row):
		for j in range(col):
			for k in range(col):
				C_mat[i][j] = C_mat[i][j] + A_mat[i][k] * B_mat[k][j]
	print("Multiplication of two matrices : ")
	for n in C_mat:
		print(n)

def tra_matrix(A_mat,B_mat,row,col):
	C_mat=[[0 for j in range(col)]for i in range(row)]
	for i in range(0,row):
		for j in range(0,col):
			C_mat[i][j] = A_mat[j][i]
	print("Transpose of first matrix matrices : ")
	for n in C_mat:
		print(n)

	for i in range(0,row):
		for j in range(0,col):
			C_mat[i][j] = B_mat[j][i]
	print("Transpose of Second matrix matrices : ")
	for n in C_mat:
		print(n)

a=True
while(a==True):
	print("**********MENU************")
	print("Enter 1 for Addition of two matrices")
	print("Enter 2 for Subtraction of two matrices")
	print("Enter 3 for Multiplication of two matrices")
	print("Enter 4 for Transpose of matrices")
	print("Enter 5 for Exit")
	choice=int(input("Enter your choice : "))

	if(choice==1):
		print(add_matrix(A_mat,B_mat,row,col))
	elif(choice==2):
		print(sub_matrix(A_mat,B_mat,row,col))
	elif(choice==3):
		print(mul_matrix(A_mat,B_mat,row,col))
	elif(choice==4):
		print(tra_matrix(A_mat,B_mat,row,col))
	elif(choice==5):
		print("Exiting.......!")
		a=False
