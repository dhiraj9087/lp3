weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

def fractional(weights, values, capacity):
    n=len(weights)
    arr = [(values[i]/weights[i],weights[i],values[i]) for i in range(n)]
    total=0
    arr.sort(reverse=True)
    for ratio, weight,value in arr:
        if capacity==0:
            break
        elif weight<=capacity:
            total+=value
            capacity-=weight
        else:
            total += value*(value/weight)
            break
    return total

print(fractional(weights,values,capacity))

