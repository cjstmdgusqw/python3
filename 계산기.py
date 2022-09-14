class Calc():
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Sum(self):
        return self.num1 + self.num2

    def Min(self):
        return self.num1 - self.num2
        
    def Mul(self):  
        return self.num1 * self.num2      

    def Div(self):
        return self.num1 / self.num2

calc = Calc(20,10)
print(calc.Sum())
print(calc.Min())
print(calc.Mul())
print(calc.Div()) 

