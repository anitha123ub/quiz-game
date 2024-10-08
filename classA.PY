class A:
    a=100
    def __init__(self,p):
        self._p=p
        
    def get_p(self):
        return self._p
        
        
    def setterA(self,p):
        self._p=p  
        
    def ironman1(self):
        print(self._p,"i am ironman 1")
        
# obj_a=A(10)
# obj_a.ironman1()


        
        
class B(A):
    b=200
    def __init__(self,p,q):
        super().__init__(p)
        self.q=q
    def ironman2(self):
        print("i am iron man2")
        
        
class C(B):
    c=300
    def __init__(self,p,q,r):
        super().__init__(p,q)
        self.r=r
        
    def ironman3(self):
        print("i am iron man 3")
        print(self._p,"is my grand father power")
        print(self.q,"is my father power")
        print(self.r,"is my own power")
        
obj_c=C(10,20,30)
obj_c.ironman3()