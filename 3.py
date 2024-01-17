def test(*args):
    for _ in range(5):
        yield 1


def solution(storages, count):
    for rest_storages in range(storages, 0, -1):
        c = count // rest_storages
        count -= c
        yield c


def check(func, a, b):
    print(list(func(a, b)))
    print(sum(list(func(a, b))))


check(solution, 5, 97)