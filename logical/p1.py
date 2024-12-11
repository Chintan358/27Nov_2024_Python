
# for j in range(1,10):

#     for i in range(1,10):
#         print('*',end="")
#     print("")

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

# starCount=1
# for i in range(1,6):
#     for j in range(starCount):
#         print("*",end=" ")
#     print("")
#     starCount+=1

# *****
# ****
# ***
# **
# *

# lines=7
# starCount=lines-1
# for i in range(1,lines):
#     for j in range(starCount):
#         print("*",end="")
#     print("")
#     starCount-=1


#     *  *****
#    **   ****
#   ***    ***
#  ****     **
# *****      *

# lines=7
# starCount=lines-1
# spaceCount = 0
# for i in range(1,lines):
#     for k in range(spaceCount):
#         print(" ",end="")
#     for j in range(starCount):
#         print("*",end="")
#     print("")
#     starCount-=1
#     spaceCount+=1

# lines=7
# starCount=1
# spaceCount = lines-1
# for i in range(1,lines):
#     for k in range(spaceCount):
#         print(" ",end="")
#     for j in range(starCount):
#         print("*",end="")
#     print("")
#     starCount+=1
#     spaceCount-=1

#    *
#   * *
#  * * *
 
# lines=7
# starCount=1
# spaceCount = lines-1
# for i in range(1,lines):
#     for k in range(spaceCount):
#         print(" ",end="")
#     for j in range(starCount):
#         print("*",end=" ")
#     print("")
#     starCount+=1
#     spaceCount-=1

#    *
#   * *
#  * * *
#   * *
#    *


lines=7
mid=(lines//2)+1
starCount=1
spaceCount = lines-1
for i in range(1,lines+1):
    for k in range(spaceCount):
        print(" ",end="")
    for j in range(starCount):
        print("*",end=" ")
    print("")
    if(mid>i):
        starCount+=1
        spaceCount-=1
    else:
        starCount-=1
        spaceCount+=1