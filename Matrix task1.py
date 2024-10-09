Matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Rotating 90 degrees towords the clockwise
Rotate_matrix_90_degrees = []
for row in range(len(Matrix)):
    sub_matrix = []
    for col in range(len(Matrix[row])-1,-1,-1):
        sub_matrix.append(Matrix[col][row])
    Rotate_matrix_90_degrees.append(sub_matrix)
print(Rotate_matrix_90_degrees)