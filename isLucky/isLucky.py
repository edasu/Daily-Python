def solution(n):
    strn = str(n)
    f = []
    s = []
    for x in list(strn[:int(len(strn) / 2)]):
        f.append(int(x))
        first_h = sum(f)
    for y in strn[int(len(strn) / 2):]:
        s.append(int(y))
        second_h = sum(s)
    return first_h == second_h

#OR
def solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
