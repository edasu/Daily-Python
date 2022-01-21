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
    strn = str(n)
    first_h = sum([int(x) for x in list(strn[:int(len(strn) / 2)])])
    second_h = sum([int(x) for x in list(strn[int(len(strn) / 2):])])
    return first_h == second_h