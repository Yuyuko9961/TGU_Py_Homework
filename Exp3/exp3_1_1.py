answer = []
for num in range(100, 1000):
    num_str = str(num)
    if num == int(num_str[0]) ** 3 + int(num_str[1]) ** 3 + int(num_str[2]) ** 3:
        answer.append(num)
print(*answer, sep=", ")

# answer = [
#     num
#     for num in range(100, 1000)
#     if num == sum(int(digit) ** len(str(num)) for digit in str(num))
# ]
