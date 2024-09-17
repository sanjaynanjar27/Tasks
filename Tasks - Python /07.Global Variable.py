class Demo():
    a = 10
    def data(self):
        print("This is function.")
        a = 20
        print(f"variable inside function : {a}")
obj = Demo()
obj.data()
print(f"Global Variable a : {obj.a}")