
data = input().rstrip().split()
rows = int(data[0])
columns = int(data[1])
r = int(data[2])


matrix = [list(map(int,input().rstrip().split())) for _ in range(rows)]

r = 1
n, m = len(matrix), len(matrix[0])
layers = min(n, m) // 2
for k in range(layers):
    layer = []
    
    for i in range(k, m - k):
        layer.append(matrix[k][i])
    
    for i in range(k + 1, n - k - 1):
        layer.append(matrix[i][m - k - 1])
    
    for i in range(m - k - 1, k - 1, -1):
        layer.append(matrix[n - k - 1][i])

    
    for i in range(n - k - 2, k, -1):
        layer.append(matrix[i][k])

    
length = len(layer)
rotation = r % length
rotated_layer = layer[rotation:] + layer[:rotation]
l = 0

for i in range(k, m - k):
    matrix[k][i] = rotated_layer[l]
    l += 1
for i in range(k + 1, n - k - 1):
    matrix[i][m - k - 1] = rotated_layer[l]
    l += 1
for i in range(m - k - 1, k - 1, -1):
    matrix[n - k - 1][i] = rotated_layer[l]
    l += 1
for i in range(n - k - 2, k, -1):
    matrix[i][k] = rotated_layer[l]
    l += 1

for row in matrix:
    print(" ".join(map(str, row)))
