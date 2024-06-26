n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = -1e9 # 초기 값, 재귀를 거치며 최대값이 계속 업데이트 됨
mini = 1e9 # 초기 값, 재귀를 거치며 최소값이 계속 업데이트 됨

def dfs(depth, total, plus, minus, multi, divide):
    global maxi, mini
    if depth == n: # 모든 사칙연산을 전부 배치했다면
        maxi = max(total, maxi) # 최대값
        mini = min(total, mini) # 최소값
        return
        
    # depth != n 인 경우 재귀 처리
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus, minus, multi, divide-1)
        # total//num[depth] 사용 시 음수의 나눗셈에서 문제 제시 조건대로 몫을 내지 않음

dfs(1, num[0], op[0], op[1], op[2], op[3]) # total 초기값은 nums[0]
print(maxi)
print(mini)