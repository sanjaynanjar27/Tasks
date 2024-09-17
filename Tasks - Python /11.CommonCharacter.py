# Using comprehension

count = 1
word = input('Enter Letters')
cd = {}
d = {x : word.count(x) for x in set(word)}


# Using Loop

for i in word:
    if i in cd:
        cd[i] += 1
    else:
        cd[i] = 1
print(cd)
for key,  val in cd.items():
    print(key,  val)
