def solution(n):
    if n >10**4 or n < 1:
        return False
    else:
        return(n**2+(n-1)**2)