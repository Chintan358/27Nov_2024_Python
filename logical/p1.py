
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


# lines=7
# mid=(lines//2)+1
# starCount=1
# spaceCount = lines-1
# for i in range(1,lines+1):
#     for k in range(spaceCount):
#         print(" ",end="")
#     for j in range(starCount):
#         print("*",end=" ")
#     print("")
#     if(mid>i):
#         starCount+=1
#         spaceCount-=1
#     else:
#         starCount-=1
#         spaceCount+=1


# lines=7
# mid=(lines//2)+1
# starCount=1
# spaceCount = lines-1
# for i in range(1,lines+1):
#     for k in range(1,spaceCount+1):
#         print(" ",end="")
#     for j in range(1,starCount+1):
#         if j==1 or j==starCount:
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print("")
#     if(mid>i):
#         starCount+=1
#         spaceCount-=1
#     else:
#         starCount-=1
#         spaceCount+=1


# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()
# for i in range(1,6):
#     for k in range(1,i+1):
#         print(" ",end="")
#     for j in range(5,i,-1):
#         print("* ",end="")
#     print()



# lines=7
# starCount=1
# spaceCount = lines-1
# for i in range(1,lines):
#     for k in range(spaceCount):
#         print(" ",end="")
#     for j in range(starCount):
#         print("*",end="")
#     print("")
#     starCount+=2
#     spaceCount-=1


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# starCount=1
# for i in range(1,6):
#     for j in range(1,starCount+1):
#         print(j,end=" ")
#     print("")
#     starCount+=1


# 1
# 2 3 
# 4 5 6
# 7 8 9 10

# num=1
# for j in range(10):
#     for i in range(j+1):
#         print(num,end=" ")
#         num=num+1
#     print("")
    


# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0


# for j in range(5):
#     for i in range(j+1):
#         print((j+i)%2,end=" ")
#     print("")
    
# A
# B C 
# D E F 
# G H I j








