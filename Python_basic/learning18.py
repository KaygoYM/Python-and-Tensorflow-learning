def fun(x):
    return x%2==0

print(list(filter(fun,range(10))))

#class
class Calculator:
    name='Casio'
    press=1
    price='18$'
    def __init__(self,price,h,w,we,name='Deli'):
        self.name=name
        self.price=price
        self.height=h
        self.width=w
        self.weight=we
        self.print_name()
    def plus(self,x,y):
        print('x+y=',x+y)
        return x+y

    def minus(self,x,y):
        print('x-y=',x-y)
        return x-y
        
    def times(self,x,y):
        print('x*y=',x*y)
        return x*y

    def divide(self,x,y):
        print('x/y=',x/y)
        return x/y
        
    def print_name(self):
        print(self.name)
#c=Calculator()
#c=Calculator(12,56,888,999)
