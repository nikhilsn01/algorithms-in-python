def generate_adjacency_matrix(v):
    matrix = list()
    for i in range(v):
        matrix.append([0 for i in range(v)])
    edges = int(input("Enter number of edges\n"))
    for i in range(edges):
        i,v = map(int,input("enter the vertices of edge   ").split())
        matrix[i-1][v-1] = 1;
    return matrix

vertices = int(input("Enter number of vertices of a matrix  "))
matrix = generate_adjacency_matrix(vertices)

for i in range(vertices):
    for j in range(vertices):
        for k in range(vertices):
            if (matrix[j][i]==1)and(matrix[i][k]==1):
                    matrix[j][k] = 1
                    print(i,j,k)



for i in matrix:
    print(i)

