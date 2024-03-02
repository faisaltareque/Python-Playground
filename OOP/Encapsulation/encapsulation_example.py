class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self._b = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
class Derived(Base): 
    def __init__(self): 
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._b) 
        print("Calling private member of base class: ") 
        print(self.__c) 
  

obj1 = Base() 
print(obj1.a)
print(obj1._b)
  
# Uncommenting print(obj1.c) will 
# raise an AttributeError
# print(obj1.c)
# print(obj1.__c)  
  
# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 
# obj2 = Derived()