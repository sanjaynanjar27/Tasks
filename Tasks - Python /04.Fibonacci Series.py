# program to print Fibonacci sequence
a = 0
b = 1
total = 0
num = int(input("Enter Range Of Your series"))
print(a, b)
for i in range(2, num):
    total = a + b
    a = b = total
    print(total,  end=" ")