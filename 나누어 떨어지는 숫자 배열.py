def solution(arr, divisor):
    answer = []
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            answer.sort()
    if not answer:
        return [-1]
    return answer