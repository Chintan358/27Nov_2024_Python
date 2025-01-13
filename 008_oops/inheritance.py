# parent - super - base
class Pen:

    
    def __init__(self,color,company):
        self.color = color
        self.company=company

    def toWrite(self):
        print(self.color, self.company)


class Slat:
    def __init__(self,color):
        self.color = color

    def show(self):
        print("self calling : ",self.color)


#child-sub-derived
class Notebook(Pen,Slat):
    
    def __init__(self,color,company):
        Pen.__init__(self,color,company)
        Slat.__init__(self,color)

    def disp(self):
        print("display calaing",self.color,self.company)
    



n  =Notebook("Red","Cello")
n.toWrite()
n.disp()
n.show()