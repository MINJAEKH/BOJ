T = int(input())

for _ in range(T) :
    vps_stack = []
    flag = True 

    for char in input().strip() :
        if char == '(' :
            vps_stack.append(char)
        elif char == ')' :
            if len(vps_stack) == 0 :
                # print(char, ":", len(vps_stack) )
                flag = False
                break
            vps_stack.pop()

    #print(flag, vps_stack)
    if flag and len(vps_stack) == 0 :
        print("YES")
    else :
        print("NO")

