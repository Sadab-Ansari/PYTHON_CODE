def is_ramanujan(num):
    pairs = []
    limit = int(num ** (1/3)) + 1

    for i in range(1, limit):
        for j in range(i, limit):
            if i**3 + j**3 == num:
                pairs.append((i, j))

    return len(pairs) >= 2

num = int(input("Enter a number to check if it's a Ramanujan number: "))

if is_ramanujan(num):
    print(f"{num} is a Ramanujan number.")
else:
    print(f"{num} is not a Ramanujan number.")
