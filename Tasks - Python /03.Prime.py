ls= [2]
st = int(input('Enter Yur Starting point'))
ep = int(input('Enter Yur Ending point'))
for i in range(st,ep):
    for j in range(2,i):
        if (i % j) != 0:
            ls.append(i)
        break
print(ls)