
class Student:

    a = 10
    b = 20

    def __init__(self,*a):
        print("const calling",a)

    def display(self):
        print("display calling",self.a,self.b)

    def add(self,a,b):
        print(a+b)
    
    @staticmethod
    def test():
        print("Test method calling.")



s =Student()
s.a=50
s.display()


s1 = Student()
s1.display()

s2 = Student()
s2.display()

Student.test()