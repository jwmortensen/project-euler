triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

n = len(triangle)

triangle_sum = [[0 for i in range(j + 1)] for j in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(0, i + 1):
        if i == n - 1:
            triangle_sum[i][j] = triangle[i][j]
        else:
            triangle_sum[i][j] = triangle[i][j] + max(
                triangle_sum[i + 1][j], triangle_sum[i + 1][j + 1])

print(triangle_sum)

path = [0 for i in range(n)]

for i in range(1, n):
    if triangle_sum[i][path[i - 1]] > triangle_sum[i][path[i - 1] + 1]:
        path[i] = path[i - 1]
    else:
        path[i] = path[i - 1] + 1

print(path)

