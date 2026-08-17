#stack implementation using array
arr = [0] * 5

print("Enter 5 elements:")
for i in range(5):
    arr[i] = int(input(f"Element {i+1}: "))

top = len(arr) - 1

while top >= 0:
    print("Deleted Element:", arr[top])

    print("Current Array:", end=" ")
    for i in range(top):
        print(arr[i], end=" ")
    print()

    top -= 1

print("Array cleared successfully.")

# Queue implementation using array

arr = [0] * 5

print("Enter 5 elements:")
for i in range(5):
    arr[i] = int(input(f"Element {i+1}: "))

front = 0
rear = len(arr) - 1

while front <= rear:
    print("Deleted Element:", arr[front])

    print("Current Array:", end=" ")
    for i in range(front + 1, rear + 1):
        print(arr[i], end=" ")
    print()

    front += 1

print("Array cleared successfully.")