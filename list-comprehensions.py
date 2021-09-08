X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

result = []

for a in range(0, X + 1):
    for b in range(0, Y + 1):
        for c in range(0, Z + 1):
            if (a + b + c) != N:
                result.append([a, b, c])

print(result)
