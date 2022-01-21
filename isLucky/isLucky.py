def solution(n):
    strn = str(n)
    first_h = sum([int(x) for x in list(strn[:int(len(strn) / 2)])])
    second_h = sum([int(x) for x in list(strn[int(len(strn) / 2):])])
    return first_h == second_h

#OR
def solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
