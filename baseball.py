import random
import time
from datetime import datetime, timedelta

C = 0
N = int(input()) # 몇자리 숫자인지
M = [0,1,2,3,4,5,6,7,8,9]

start_time = time.time()

random.shuffle(M)
r_list = M[:N]


while True:
    
    A = (input("정답을 입력해 주세요"))
    if A == 'exit':
        break
    
    A_list = []
    for i in A:
        A_list.append(int(i))
    A = A_list

    C = C + 1

    strike_count = 0
    ball_count  = 0
    out_count = 0
    out = 0

    time.sleep(1)
    
    for i in range(0,N):
        for j in range(0,N):
            if r_list[i] == A[j]:
                if i == j:
                    strike_count += 1
                else : 
                    ball_count += 1
            elif r_list[i] != (A[j]):
                out +=1
                if out == N*N:
                    out_count +=1
                else:
                    continue   
             
    print(f"{strike_count} strike {ball_count} ball {out_count} out")           
    
    end_time = time.time()
    
    if strike_count == N:
        print(f"{C}번만에 맞추셨습니다")
        print(f"기록 : {end_time-start_time:.2f}초")
        print(datetime.now())
        break
    elif A == "exit":
        break


              

        
    
    

