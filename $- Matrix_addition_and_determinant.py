rows = int(4)
cols = int(4)
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"{i+1}.sıra ,{j+1}.sütun için değer gir: "))
        row.append(value)
    matrix.append(row)
    
print("1. Matrix")
for row in matrix:
    print(row) 
print("-"*50)

print("2. Matrix için; ")
rows1 = int(4)
cols1 = int(4)
matrix1 = []
for i1 in range(rows1):
    row1 = []
    for j1 in range(cols1):
        value1 = int(input(f"{i1+1}.sıra ,{j1+1}.sütun için değer gir: "))
        row1.append(value1)
    matrix1.append(row1)

print("2. Matrix")
for row1 in matrix1:
    print(row1)

print("-"*50)
for row in matrix:
    print(row)  
print("-"*50)
for row1 in matrix1:
    print(row1)
    

print("İki matrixin toplamı: ")
top_mat=[ [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix1[0])):
        top_mat[i][j] = matrix[i][j] + matrix1[i][j]
        
for row in top_mat:
    print(row)
    
det_A1 = top_mat[1][1] * top_mat[2][2] * top_mat[3][3] + top_mat[1][2] * top_mat[2][3] * top_mat[3][1] + top_mat[1][3] * top_mat[2][1] * top_mat[3][2] - top_mat[1][1] * top_mat[2][3] * top_mat[3][2] - top_mat[1][2] * top_mat[2][1] * top_mat[3][3] - top_mat[1][3] * top_mat[2][2] * top_mat[3][1]


det_A2 = top_mat[1][0] * top_mat[2][2] * top_mat[3][3] + top_mat[1][2] * top_mat[2][3] * top_mat[3][0] + top_mat[1][3] * top_mat[2][0] * top_mat[3][2] - top_mat[1][0] * top_mat[2][3] * top_mat[3][2] - top_mat[1][2] * top_mat[2][0] * top_mat[3][3] - top_mat[1][3] * top_mat[2][2] * top_mat[3][0]


det_A3 = top_mat[1][0] * top_mat[2][1] * top_mat[3][3] + top_mat[1][1] * top_mat[2][3] * top_mat[3][0] + top_mat[1][3] * top_mat[2][0] * top_mat[3][1] - top_mat[1][0] * top_mat[2][3] * top_mat[3][1] - top_mat[1][1] * top_mat[2][0] * top_mat[3][3] - top_mat[1][3] * top_mat[2][1] * top_mat[3][0]


det_A4 = top_mat[1][0] * top_mat[2][1] * top_mat[3][2] + top_mat[1][1] * top_mat[2][2] * top_mat[3][0] + top_mat[1][2] * top_mat[2][0] * top_mat[3][1] - top_mat[1][0] * top_mat[2][2] * top_mat[3][1] - top_mat[1][1] * top_mat[2][0] * top_mat[3][2] - top_mat[1][2] * top_mat[2][1] * top_mat[3][0]

det_A= top_mat[0][0] * det_A1 - top_mat[0][1] * det_A2 + top_mat[0][2] * det_A3 - top_mat[0][3] * det_A4

print(det_A)
