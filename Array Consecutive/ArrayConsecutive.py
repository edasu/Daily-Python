def solution(statues):
    n = 0
    statues.sort()
    for i in range(0, len(statues ) - 1):
        if statues[i + 1] - statues[i] > 1:
            n += statues[i + 1] - statues[i] - 1
    return n