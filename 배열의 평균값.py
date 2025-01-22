def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i] 
    return sum/len(numbers)
numbers = [1,2,3,4,5,6,7,8,9,10]
print(solution(numbers))
numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(solution(numbers))