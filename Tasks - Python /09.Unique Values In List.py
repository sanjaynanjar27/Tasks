size = int(input("Enter A Series Highest : "))
data = []
dup= []
print('Enter Values')
for i in range(1, size+1):
    a = int(input())
    if a > 0:
        if a not in data:
            data.append(a)
        else:
            dup.append(a)
    for i in dup:
        if i in dup:
            data.remove(i)
            for j in data:
                print(f"Unique Value : {j}")
    print(data)