# Q 1: Maximum Sum of a Subarray of Size K

n = int(input("Enter the size of the array: "))
k = int(input("Enter the size of the subarray: "))
a = list(map(int, input("Enter the elements of the array: ").split()))

window = sum(a[:k])
maximum = window
for i in range(k, n):
    window += a[i]
    window -= a[i - k]

    if window > maximum:
        maximum = window

print("Maximum sum of a subarray of size", k, "is:", maximum)

# Q 2: Given a string S, find the length of the longest substring without repeating characters.

s = str(input("Enter the string: ").strip())

seen = set()
left = 0
answer = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    if length > answer:
        answer = length

print("Length of the longest substring without repeating characters is:", answer)

# Q.3: You are given a weighted, undirected graph with N nodes and M edges. Find the shortest 
#      path from node 1 to node N such that the path uses at most K edges. If no such path exists, output -1.

n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))
k = int(input("Enter the maximum number of edges in the path: "))

edges = []

for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    edges.append((u, v, w))

inf = float('inf')
dp = [inf] * (n + 1)
dp[1] = 0

for _ in range(k):
    new_dp = dp.copy()

    for u, v, w in edges:
        if dp[u] != inf:
            value = dp[u] + w

            if value < new_dp[v]:
                new_dp[v] = value

        if dp[v] != inf:
            value = dp[v] + w

            if value < new_dp[u]:
                new_dp[u] = value

    dp = new_dp

if dp[n] == inf:
    print(-1)
else:
    print(dp[n])
