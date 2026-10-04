# Shivam Kumar
# CU25250031
# Roll : 54 sec: A 

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    positive = 0
    negative = 0

    for x in a:
        if x > 0:
            positive += x
        else:
            negative += x

    # Number of operations is fixed by the total sum
    operations = -total

    # If operations would be negative, it is impossible
    if operations < 0:
        return -1

    # We need enough -1 operations to remove all positive values
    if positive > operations:
        return -1

    # We also need enough +2 operations to remove the negative values
   
    if -negative > 2 * operations:
        return -1

    return operations


t = int(input())

for _ in range(t):
    print(solve())
