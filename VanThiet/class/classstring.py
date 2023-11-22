class khanh:
    def __init__(self,a):
        self.a=a
    def inputs(self):
        self.a=input()
    def prints(self):
        print(self.a)
    def printbinhphuong(self):
        print(int(self.a)**2)
n=''
b=khanh(n)
b.inputs()
b.printbinhphuong()