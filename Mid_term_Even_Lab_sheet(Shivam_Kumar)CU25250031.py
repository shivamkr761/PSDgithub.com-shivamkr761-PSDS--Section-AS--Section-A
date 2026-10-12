# shivam  Kumar  54  CU25250031

# Ouestion:
# Given an array of integers, denoted as , and an integer , your task is to implement a sorting algorithm. The goal is to arrange the elements in based on their Hamming Distance from the integer .
# The Hamming Distance is defined as the count of differing bits in the binary representations of two integers.
# The sorting should be done in ascending order of Hamming distance, and in case of a tie in Hamming Distances, the elements should be sorted in ascending numerical order.
# Input Format:
# Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).
# The first line contains denoting the number of test cases. also specifies the number of times you have to run the solve function on a different set of inputs. For each test case:
# •	The first line contains the integer  and .
# •	The second line contains the array  of length 
# Output Format: For each test case, print the answer in a new line. 
# Constraints:
# Examples
# Input
# 1
# 3 2
# 4 5 6
# Output
# 6 4 5
# Explanation
# In the example, binary representation of is "". Similarly for array , the binary representation is . Now the hamming distance of each element of the array with are . Hence sorting on the basis of Hamming Distance, the final output comes out to be .



t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    dist = []

    for a in arr:
        bits = bin(a ^ x).count('1')
        dist.append((bits, a))

    dist.sort()

    for bits, a in dist:
        print(a, end=" ")
    print()

