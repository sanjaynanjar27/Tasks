def find_factorial(n):
    if n == 0:
        return  1
    else:
        return n * find_factorial(n-1)
print(find_factorial(5))
