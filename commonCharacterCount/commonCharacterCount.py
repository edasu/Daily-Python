def solution(s1, s2):
    lst = []
    for i in set(s1):
       cont =  min(s1.count(i), s2.count(i))
       lst.append(cont)
    return sum(lst)