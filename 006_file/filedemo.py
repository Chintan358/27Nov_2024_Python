# f = open("home.txt",'w')
# f.write("Hello Python")

# f = open("home.txt",'a')
# f.write("Hello Python")

# f = open("home.txt")
# data = f.read()
# print(data)
# f.close()


# with open("home.txt","r") as f : 
#     data = f.read()
#     print(data)


# with open("home.txt") as f:
#     print(f.tell())
#     f.seek(5)
#     print(f.tell())
#     data = f.read()
#     print(data)

# with open("home.txt") as f :
#     while True:
#         data=f.readline().strip()
#         if data=="Hello Python":
#             print(data)
#         if not data:
#             break

with open("home.txt","r+") as f : 
    # f.write("Hello")
    # f.seek(0)
    data = f.read()
    print(data)