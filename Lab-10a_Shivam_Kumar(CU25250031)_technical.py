# Shivam Kumar
# CU25250031
# Roll : 54 sec: A 

def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10
        num = num // 10

    return total


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    count = {}

    for x in nums:
        s = digit_sum(x)

        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    answer = 0

    for value in count.values():
        answer += value * value

    return answer

print(solve())