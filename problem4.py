def print_factors(x):
    sum = 0
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            if x == i:
                break
            sum = sum + i
            factors.append(i)
    print(f"Factor: {factors}")
    if sum == x:
        print(f"{x} is a perfect number")
    else:
        print(f"{x} is not a perfect number")

user_num = int(input("Input number: "))
print_factors(user_num)