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


try:
    i, j = map(int, input().split())
    calc = Calc(i,j)
    print(calc.Sum())
    print(calc.Min())
    print(calc.Mul())
    print(calc.Div()) 

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

except Exception as e:
    print("숫자만 입력 가능합니다")   