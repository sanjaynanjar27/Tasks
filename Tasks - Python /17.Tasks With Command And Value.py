
if __name__ == '__main__':
    N = int(input())
    data=[]
    for i in range(N):
        query = input("").lower().split(" ")
        if 'insert' in query:
            data.insert(int(query[1]),int(query[2]))
        elif 'append' in query:
            data.append(int(query[1]))
        elif 'remove' in query:
            data.remove(int(query[1]))
        elif 'sort' in query:
            data.sort()
        elif 'reverse' in query:
            data.reverse()
        elif 'pop' in query:
            data.pop()
        elif 'print' in query:
            print(data)
        else:
            print("Enter Valid Query")


# 10 - Number Of Query You want to Perform
# append 2
# insert 1 21
# append 44
# sort
# reverse
# print
# [44, 21, 2]
# append 3
# append 42
# sort
# print
# [2, 3, 21, 42, 44]