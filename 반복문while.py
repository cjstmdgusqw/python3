C = 0
while True:
    N = input()
    

    if N.isdigit() == True:
        print(int(N)*2)
        C = C + 1
        if C == 5:
            break
    elif N == "exit":
        break
    elif N.isdigit != True:
        print(f"당신은 {N}를 입력했습니다.")
  
  


    



