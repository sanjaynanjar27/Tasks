






# 14. Join Tuples if similar initial element using defaultdict.
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

from collections import defaultdict
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
grouped_dict = defaultdict(list)
print( grouped_dict)
for tpl in test_list:
    grouped_dict[tpl[0]].extend(tpl[1:])
    print(grouped_dict)
result = [(key,) + tuple(value) for key, value in grouped_dict.items()]

print(result)


# Output :
# defaultdict(<class 'list'>, {})
# defaultdict(<class 'list'>, {5: [6]})
# defaultdict(<class 'list'>, {5: [6, 7]})
# defaultdict(<class 'list'>, {5: [6, 7, 8]})
# defaultdict(<class 'list'>, {5: [6, 7, 8], 6: [10]})
# defaultdict(<class 'list'>, {5: [6, 7, 8], 6: [10], 7: [13]})
# [(5, 6, 7, 8), (6, 10), (7, 13)]