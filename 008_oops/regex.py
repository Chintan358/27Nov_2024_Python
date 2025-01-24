import re

# Nameage="""Rany is 23 and Jeny is 65, Tom is 85 And Roy is 42 """

# age=re.findall(r'\d{1,5}',Nameage)

# names=re.findall(r'[A-Z][a-z]*',Nameage)
# names=re.findall(r'[a-z]*',Nameage)
# names=re.findall(r'[A-Z][a-z]*',Nameage)
# print(age)
# print(names)

# str = "is oops python"
# # k = re.search("python",str)
# k = re.match("python",str)
# print(k)


# name="Python is world's best programming language "
# for i in re.finditer("world's",name):
#     print(i)
#   ans=i.span()
#   print(ans)


# import re
# word="dog, bot , god , rose , snot,ot "
# regex=re.compile("[a-z]*ot")
# word=regex.sub("Sample",word)
# print(word)

# pettern = "^[a-zA-Z0-9]+@[a-z]+.[a-z]{2,4}$"
# email = "test@yahoo.com"


# x = re.match(pettern,email)
# if x is None:
#     print("invalid email")
# else : 
#     print("valid")

# pettern = "^[0-9]{10}$"
# phone = "9099614545"


# x = re.match(pettern,phone)
# if x is None:
#     print("invalid phone")
# else : 
#     print("valid")