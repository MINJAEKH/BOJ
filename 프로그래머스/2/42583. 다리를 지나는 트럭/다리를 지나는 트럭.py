from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0]*bridge_length)
    
    while on_bridge :
        time += 1
        total -= on_bridge.popleft()
        
        if truck_weights : 
            if truck_weights[0] + total <= weight :
                next_truck = truck_weights.popleft()
                on_bridge.append(next_truck)
                total += next_truck
            else :
                on_bridge.append(0)        
    return time