
sub = {
    "101":"Java",
    "102":"Python",
    "101":"Node"
}

person = {
    "1":"Ankit",
    "2":"Khadija"
}

# print(sub['101'])
# print(sub.get("102"))
# print(sub.keys())
# sub['105']="React"
# print(sub.keys())

# print(sub.items())

# sub.update(person)
# print(sub)

# for i in sub.values():
#     print(i)

# for x,y in sub.items():
#     print(x,y)

student = {
    "name ":"ankit",
    "email":"anlit@gmail.com",
    "address":{
        "city":"surat",
        "state":"gujarat"
    }
}

# print(student['address']['city'])

for i,obj in student.items():
    print(i)
    print(obj)