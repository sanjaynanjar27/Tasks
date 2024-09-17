# 11. Python program to extract only the numbers from a lst which have some specific digits using Using filter() + lambda
# Input : test_list = [3456,  23,  128,  235,  982],  dig_list = [2,  3,  5,  4]
test_list = [3456,  23,  128,  235,  982]
dig_list = [2,  3,  5,  4]
ls = []
for i in test_list:
    for j in dig_list:
        if str(j) in str(i):
            ls.append(i)
        break
print(ls)
