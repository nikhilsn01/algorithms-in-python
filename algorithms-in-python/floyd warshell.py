def generate_distance_matrix(v):
    matrix = list()
    for i in range(v):
        print("Enter row",i+1,"values")
        row = []
        for j in range(v):
            value = input()
            if value=="i":
                row.append(99999)
            else:
                row.append(int(value))
        matrix.append(row)
    return matrix

vertices = int(input("Enter number of vertices of a matrix  "))
matrix = generate_distance_matrix(vertices)

for i in range(vertices):
    for j in range(vertices):
        for k in range(vertices):
            if (matrix[j][i]==1)+(matrix[i][k]==1):
                    matrix[j][k] = 1
                    print(i,j,k)



for i in matrix:
    print(i)

