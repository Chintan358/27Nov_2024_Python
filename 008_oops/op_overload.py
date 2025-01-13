
class Demo : 

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,other):
        return  self.a+other.a,self.b+other.b
    
    def __mul__(self,other):
        return self.a*other.a,self.b*other.b



d1 = Demo(10,20)
d2 = Demo(20,30)

c = d1 + d2
k = d1*d2
print(c)
print(k)