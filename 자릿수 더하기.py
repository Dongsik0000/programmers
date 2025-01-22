def solution(n):
    answer = 0
    numbers = []
    str_num = str(n)
    for i in range(len(str_num)):
        answer += int(str_num[i])
    return answer