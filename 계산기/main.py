num1, num2 = map(int,input("숫자를 2개 입력해주세요 : ").split())
operator = input("문자를 입력해 주세요 : (+,-,*,/) : ") #split를 붙일 필요가 없다!


if operator == '+':
    import add
    add.add_function(num1, num2) 
elif operator == '-':
    import min
    min.min_function(num1, num2)    
elif operator == '*':
    import mul
    mul.mul_function(num1, num2)  
elif operator == '/':
    import dev
    dev.dev_function(num1, num2)      