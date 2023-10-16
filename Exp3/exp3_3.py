prime_number = []
for i in range(20, 101):
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        prime_number.append(i)
print(*prime_number, sep=", ")
print(f"共有{len(prime_number)}个素数")
