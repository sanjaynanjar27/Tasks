
def find(n, arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count == 1:
            return num

n = int(input())
arr = list(map(int, input().split()))
print(find(n, arr))



# input : 3
# input : 1 2 1
# input : 2