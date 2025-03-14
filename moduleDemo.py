print("before")
l=[1,2]
try:
    print(l[5])
    print(10/5)
except ZeroDivisionError:
    print("ZeroDivisionError exception handled")
except IndexError:
    print("IndexError exception handled")
print("after")
