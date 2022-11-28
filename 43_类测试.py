# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:54:01 2022

@author: sun78
"""

class Dog():
    def __init__(self,txtName,x,y):
        self.txtName = txtName
        self.x = x
        self.y = y
        
    def locaXY(self):
    # self.y = y
        with open(self.txtName, 'r') as f:
            lines = f.readlines()  
            txtLength = len(lines)
            print("文本行数",txtLength ) 
            for i,j in enumerate(lines):                
                if i == self.x-1:                   
                    print(j)
                    jList = j.split( )
                    print(jList[self.y-1])
                    return jList[self.y-1]
                
                
            
            
MyDOG = Dog("c.txt",5,4)            
MyDOG.locaXY()      




            
            
            
            
"""            
    def prin(self):
        print(str(self.x))
        print(str(self.y))
    def sumxy(self):
        q = self.x + self.y
        print()
        print("求和",q)
        return q
    def divid(self):
        p = self.x / self.y
        print()
        print("x/y",p)
        return p
        # print("求和: ",xySum)

ex_1 = Dog(99,100)

ex_1.sumxy()
ex_1.prin()
ex_1.divid()
"""