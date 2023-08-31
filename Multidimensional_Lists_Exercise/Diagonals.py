N = int(input())

matrix = []

for i in range(N):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []

for idx in range(N):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][N - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
