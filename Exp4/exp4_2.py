def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
prime_number = [num for num in range(2, 101) if is_prime(num)]
print(*prime_number, sep=",", end="。\n")
print(f"共有{len(prime_number)}个素数")
