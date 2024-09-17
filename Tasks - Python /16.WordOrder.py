
# Word Order
n = int(input("Enter Number"))
dic = {}
words = []
for i in range(n):
    word = input("")
    words.append(word)
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
print(len(dic))
print(dic)



# Output: 
# Enter Number9
# a
# s
# f
# s
# a
# w
# s
# f
# s 
# 4
# {'a': 2, 's': 4, 'f': 2, 'w': 1}