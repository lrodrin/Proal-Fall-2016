def welcome(name):
    print("Hello %s, you are welcome!" % name)


def max_min(x, y):
    return "(%d, %d)" % (max(x, y), min(x, y))


def integer_division(a, b):
    if a >= 0 and b >= 0 and b != 0:
        return "(%d, %d)" % (a / b, a % b)


def digit_count(n):
    count = 1
    while (int(n / 10)) is not 0:
        count += 1
        n = int(n / 10)
    return count


# def leading_hand(h, m):
# update_arrival(h, m, d):


if __name__ == "__main__":
    welcome("King Kong")
    print(max_min(-3, 5))
    print(integer_division(14, 3))
    print(digit_count(6543))
