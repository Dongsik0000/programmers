def solution(x):  
    digits = list(str(x))  
    digit_sum = sum(int(digit) for digit in digits) 
    return x % digit_sum == 0  