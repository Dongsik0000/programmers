def solution(n):
    x = int(n ** (1/2)) 
    if x ** 2 == n:  
        return (x + 1) ** 2
    else:
        return -1