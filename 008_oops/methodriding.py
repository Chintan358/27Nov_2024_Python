
class A:

    def show(self):
        print("A : show method calling")


class B(A):

   
    def show(self):
        print("B : Show mwthod calling")
    


b  = B()
b.show()