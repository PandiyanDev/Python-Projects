def findMean(lst: list) -> float:
    return sum(lst)/len(lst)

def findMedian(lst: list) -> float:
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        left = lst[len(lst)//2]
        right = lst[len(lst)//2-1]
        median = (left + right)/2
    else:
        median = lst[len(lst)//2]
    return median

def findMode(lst: list) -> int:
    frequency = {}
    for i in lst:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    return mode
    


lst = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
print("Mean: ", findMean(lst))
print("Median: ", findMedian(lst))
print('Mode: ', findMode(lst))

