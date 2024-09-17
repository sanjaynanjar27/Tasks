
n = int(input("Enter How Many Emails You want to validate"))
print("Enter Email Address.")
check = r'\b[A-za-z0-9._%+-]+@[A-Z, a-z0-9.-]+\.[A-Z|a-z]{2, 7}\b'
data = []
for i in range(n):
    e = input("")
    if (e != " ") and (10 <= len(e) <= 80) and (re.fullmatch(check,  e)):
             data.append(e)
    else:
            print(f" {e} Is Not Valid,  Enter Valid Email")
print(data)
for mails in sorted(data):
    print(mails)
