# Q1. 3Sum Problem: Given an array of integers, find all unique triplets in the array which gives the sum of zero.

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


nums = list(map(int, input("Enter numbers: ").split()))

print(three_sum(nums))

# Q2. Fibonacci Sequence: Write a function to generate the first n numbers in the Fibonacci sequence starting from 1.

def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# Q3. Tower of Hanoi: Implement a recursive function to solve the Tower of Hanoi problem for n disks.

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')