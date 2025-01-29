

class Demo:

    __name = "Tops"
    _email = "tops@gmail.com"
    def __init__(self):
        pass

   

class Sample(Demo):

    def show(self):
        print(self.name)

    


d1  =Demo()
print(dir(d1))
print("**********************")
s1 = Sample()
print(dir(s1))
print(s1._Demo__name)
print(s1._email)

