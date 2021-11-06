
from random import randint
from sys import stdin


def read_int():
    return int(stdin.readline())


def read_array(typ):
    return list(map(typ, stdin.readline().split()))


def read_matrix(n):
    m = []
    for _ in range(n):
        row = read_array(int)
        assert len(row) == n
        m.append(row)
    return m


def mult(m, v):
    n = len(m)
    return [sum(m[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(a, b, c):
    n = len(a)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(a, mult(b, x)) == mult(c, x)


if __name__ == "__main__":
    n = read_int()
    a = read_matrix(n)
    b = read_matrix(n)
    c = read_matrix(n)
    print(freivalds(a, b, c))
