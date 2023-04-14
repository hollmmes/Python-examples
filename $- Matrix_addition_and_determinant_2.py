import random

sıra = 4
sutun = 4
matris1 = []
matris2 = []

for i in range(sıra):
    temp = []
    for j in range(sutun):
        değer = random.randint(0, 99) 
        temp.append(değer)
    matris1.append(temp)
for i in range(sıra):
    temp = []
    for j in range(sutun):
        değer = random.randint(0, 99) 
        temp.append(değer)
    matris2.append(temp)
    
print("1. matris",matris1)
print("2. matris",matris2)

print("----------------------------------------------------------------")

det=[ [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
for i in range(len(matris1)):
    for j in range(len(matris2)):
        det[i][j] = matris1[i][j] + matris2[i][j]
print("matrislerin toplamı: ",det)

print("----------------------------------------------------------------")


determinant=det[0][0] * det[1][1] * det[2][2] * det[3][3] - det[0][0] * det[1][1] * det[2][3] * det[3][2] - det[0][0] * det[1][2] * det[2][1] * det[3][3] + det[0][0] * det[1][2] * det[2][3] * det[3][1] + det[0][0] * det[1][3] * det[2][1] * det[3][2] - det[0][0] * det[1][3] * det[2][2] * det[3][1] - det[0][1] * det[1][0] * det[2][2] * det[3][3] + det[0][1] * det[1][0] * det[2][3] * det[3][2] + det[0][1] * det[1][2] * det[2][0] * det[3][3] - det[0][1] * det[1][2] * det[2][3] * det[3][0] - det[0][1] * det[1][3] * det[2][0] * det[3][2] + det[0][1] * det[1][3] * det[2][2] * det[3][0] + det[0][2] * det[1][0] * det[2][1] * det[3][3] - det[0][2] * det[1][0] * det[2][3] * det[3][1] - det[0][2] * det[1][1] * det[2][0] * det[3][3] + det[0][2] * det[1][1] * det[2][3] * det[3][0] + det[0][2] * det[1][3] * det[2][0] * det[3][1] - det[0][2] * det[1][3] * det[2][1] * det[3][0] - det[0][3] * det[1][0] * det[2][1] * det[3][2] + det[0][3] * det[1][0] * det[2][2] * det[3][1] + det[0][3] * det[1][1] * det[2][0] * det[3][2] - det[0][3] * det[1][1] * det[2][2] * det[3][0] - det[0][3] * det[1][2] * det[2][0] * det[3][1] + det[0][3] * det[1][2] * det[2][1] * det[3][0]
print("Toplanan 2 matrisin determinantı: ",determinant)
