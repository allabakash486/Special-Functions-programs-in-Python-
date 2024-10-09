#This program is used for creating the matrix and taking inputs from user at runtime.
length_matrix = int(input('enter the Matrix length:'))
length_row = int(input('enter the row length:'))
l = [[int(input('enter the elemnt:')) for j in range(length_row)] for i in range(length_matrix )]
print(l)