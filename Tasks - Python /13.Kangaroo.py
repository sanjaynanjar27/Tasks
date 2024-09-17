
# Kangaroo Problem
k1 = int(input("Enter First Kangaroo Position."))
v1 = int(input("Enter First Kangaroo Steps."))
k2 = int(input("Enter Second Kangaroo Position."))
v2 = int(input("Enter second Kangaroo Steps."))
if k1 > k2 and v1 > v2:
    print("No")
if k1 < k2 and v1 < v2:
    print("No")
if v1 == v2:
    print("No")
if (k2 - k1) % (v1 - v2) == 0:
    print("Yes")
else:
    print("No")
