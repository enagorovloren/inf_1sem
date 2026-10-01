a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())


def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + f(n // i)
    else:
        return [n]


def my_gcd(a, b):
    res = 1
    ar = f(a)
    br = f(b)
    for i in ar:
        if i in br:
            res *= i
            br.remove(i)
    return res


def euclid(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = euclid(b, a % b)
    return y, x - (a // b) * y, d


def solve(a, b):
    d = my_gcd(a, b)

    A, B = a // d, b // d
    x0, y0, p = euclid(A, B)

    ks = {0}
    for num, den in [(-x0, B), (y0, A)]:
        q = num // den
        for k in range(q - 2, q + 3):
            ks.add(k)

    best_key = None
    bx = by = None
    for k in ks:
        x = x0 + B * k
        y = y0 - A * k
        key = (abs(x) + abs(y), x)
        if best_key is None or key < best_key:
            best_key = key
            bx, by = x, y

    return bx, by, d


print(solve(a1,b1))
print(solve(a2,b2))