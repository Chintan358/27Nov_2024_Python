
x = 10
print(x)

def test():
    global x
    x = 20
    # y = 30
    print(x)

print(f"global : {x}")
test()
print(f"global : {x}")
# print(f"local : {y}")