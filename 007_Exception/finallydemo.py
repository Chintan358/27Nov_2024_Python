
def test():
    try:
        a = int(input("Enter number : "))
        return 1
    except:
        print("err")
        return 0
    finally:
        print("Finally called")
    print("always called")


a = test()
print(a)