from itertools import count


digits = int(input("Enter Size Of Digits"))
num = int(input("Enter Range Of Your series"))
total = 0
data = []

for i in str(num):
    data.append(int(i) ** digits)
# print(sum(data))
# print(len(data))

if len(data) == digits:
    if sum(data) == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

else:
    print("Enter Valid Digit Number")