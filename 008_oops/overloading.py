from multipledispatch import dispatch

class Calc:
  
    @dispatch(int,int,int)
    def add(self,a,b,c):
       return a+b+c
    
    @dispatch(int,int)
    def add(self,a,b):
       return a+b




c  =Calc()
a = c.add(10,20)
b = c.add(10,20,30)
print(a,b)


c1  =Calc()
a = c1.add(10,200)
b = c1.add(10,20,300)
print(a,b)