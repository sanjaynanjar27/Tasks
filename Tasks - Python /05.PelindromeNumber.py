num1 = int(input("Enter Number TO Check"))
st = ''
num2 = num1
for i in str(num1):
    st = i + st
print(st)
if int(st) == num2:
    print("Number Is Palindrome")
else:
    print("Number Is Not Palindrome")