# 12. Extract tuples having K digit elements using map fuction
# Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2 
# Input list and K


test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
K = 2
def data(nums, k):
    return all(len(str(item)) == k for item in nums)
result = list(filter(lambda nums: data(nums, K), test_list))
print(result)

# Output : [(34, 55), (12, 45), (78,)] 
