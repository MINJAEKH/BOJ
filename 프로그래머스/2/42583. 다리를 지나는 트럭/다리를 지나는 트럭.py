from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)   # 대기 트럭
    on_bridge = deque([0]*bridge_length)   # 현재 다리를 지나는 트럭 순서
    curr_weight = 0 # 현재 다리 위 무게
    
    while on_bridge :
        time += 1
        
        curr_weight -= on_bridge.popleft() # 맨 앞에 위치한 트럭이 다리를 지난 후 무게
        
        if truck_weights :
            if curr_weight + truck_weights[0] <= weight :
                next_truck = truck_weights.popleft() 
                on_bridge.append(next_truck)
                curr_weight += next_truck
            else :
                on_bridge.append(0) # 트럭 자리 이동
    return time