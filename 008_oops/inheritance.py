# parent - super - base
class Pen:

    color="Red"
    company="Cello"
    def __init__(self):
        pass

    def toWrite(self):
        print("write calling")

#child-sub-derived
class Notebook(Pen):
    
    def __init__(self):
        pass

    def disp(self):
        print("display calaing",self.color,self.company)

n  =Notebook()
n.toWrite()
n.disp()