def solution(inputArray):
    list = []
    for a in inputArray:
        if len(a) == len(max(inputArray, key=len)):
            list.append(a)
    return list

#OR

def solution(inputArray):
    return [ a for a in inputArray if len(a) == len(max(inputArray, key=len))]