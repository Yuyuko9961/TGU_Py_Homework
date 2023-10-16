answer = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            num = i * 100 + j * 10 + k
            if num == i**3 + j**3 + k**3:
                answer.append(num)
print(*answer, sep=", ")
