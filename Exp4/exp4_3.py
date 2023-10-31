def gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
def lcm(n1: int, n2: int) -> int:
    return n1 * n2 // gcd(n1, n2)
a, b = map(int, input("请输入两个正整数: ").split())
print(f"这两个正整数的最大公约数是{gcd(a, b)}, 最小公倍数是{lcm(a, b)}")
