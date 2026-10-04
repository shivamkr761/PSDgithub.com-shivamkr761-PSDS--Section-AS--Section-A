# Q1. Implement a heap (min/max) and use it to build a priority queue; perform heap sort on an array of elements.
class MyHeap:
    def __init__(self):
        self.a = []

    def add(self, x):
        self.a.append(x)
        i = len(self.a) - 1

        while i > 0:
            p = (i - 1) // 2

            if self.a[p] <= self.a[i]:   
                break

            self.a[p], self.a[i] = self.a[i], self.a[p]
            i = p

    def remove(self):
        if len(self.a) == 0:
            return None

        x = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()

        i = 0

        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            small = i

            if l < len(self.a) and self.a[l] < self.a[small]:
                small = l

            if r < len(self.a) and self.a[r] < self.a[small]:
                small = r

            if small == i:
                break

            self.a[i], self.a[small] = self.a[small], self.a[i]
            i = small

        return x


h = MyHeap()

numbers = [17, 6, 25, 3, 14, 9]

for value in numbers:
    h.add(value)

print("Heap after inserting values:", h.a)

print("Priority queue order:")
while h.a:
    print(h.remove(), end=" ")

print()

arr = [11, 4, 19, 2, 8, 15]

h = MyHeap()

for value in arr:
    h.add(value)

sorted_arr = []

while h.a:
    sorted_arr.append(h.remove())

print("Array before sorting:", arr)
print("After heap sort:", sorted_arr)

# Q.2: Rearrange Array to Maximize Adjacent Sum Difference Given an array of n integers,
#      rearrange the elements such that the sum of absolute differences between every pair 
#      of adjacent elements is maximized. Print the rearranged array along with the total 
#      sum of absolute differences.

def maximize_difference(arr):
    arr.sort()
    n = len(arr)

    if n <= 1:
        return arr, 0

    ans = [0] * n
    left = 0
    right = n - 1

    for i in range(1, n, 2):
        ans[i] = arr[right]
        right -= 1

  
    for i in range(2, n, 2):
        ans[i] = arr[left]
        left += 1

  
    ans[0] = arr[left]
    left += 1
    ans[n - 1] = arr[left]

    total = 0

    for i in range(1, n):
        total += abs(ans[i] - ans[i - 1])

    return ans, total


arr = [4, 2, 7, 1]

result, total = maximize_difference(arr)

print("Original array:", arr)
print("Rearranged array:", result)
print("Maximum sum:", total)

# Q.3: Smallest Subarray with Sum Greater Than Target Given an array of n positive 
#      integers and an integer target, find the length of the smallest contiguous subarray 
#      whose sum is strictly greater than target. If no such subarray exists, return -1.

def find_smallest(a, target):
    start = 0
    total = 0
    answer = len(a) + 1

    for end in range(len(a)):
        total = total + a[end]

        while total > target:
            size = end - start + 1

            if size < answer:
                answer = size

            total = total - a[start]
            start += 1

    if answer == len(a) + 1:
        return -1

    return answer


a = [5, 1, 2, 1, 3, 2, 6, 2]
target = 9

ans = find_smallest(a, target)

print("Numbers:", a)
print("Target:", target)
print("Smallest subarray length:", ans)