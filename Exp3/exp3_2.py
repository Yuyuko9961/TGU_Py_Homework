a, b = map(int, input("输入两个正整数: ").split())
product = a * b
while b != 0:
    a, b = b, a % b
print(f"这两个正整数的最大公约数是{a}, 最小公倍数是{product//a}")
