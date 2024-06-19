M = int(input()) ; N = int(input())

prime_list = []

for num in range(M, N + 1):
    if num > 1 :
        flag = True 
        for i in range(2, num // 2 +1 ) :
            if num % i == 0 :
                flag = False 
                break
        if flag == True :
            prime_list.append(num)
if len(prime_list) == 0 :
    print(-1)
else :
    print(sum(prime_list))
    print(min(prime_list))

