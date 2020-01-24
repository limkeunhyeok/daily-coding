def solution(bridge_length, weight, truck_weights):
    temp = [0] * bridge_length
    count = 0
    while temp:
        count += 1
        temp.pop(0)
        if truck_weights:
            if sum(temp) + truck_weights[0] <= weight:
                temp.append(truck_weights.pop(0))
            else:
                temp.append(0)
    return count