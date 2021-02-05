import time

def solution(n, arr):
    min=1000000
    max=-1000000
    arr=arr.split(' ')
    for i in range(n):
        arr[i]=int(arr[i])
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]
    answer = str(min) + ' ' + str(max)
    return answer


n = int(input())
arr = input()

start_time = time.time()
answer = solution(n, arr)
end_time = time.time()

print(answer)
print("time: ", end_time-start_time)