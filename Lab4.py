# stack
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')
print(stack)
print("Lenght ",len(stack))
print("Top Element",stack[-1])
print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('Stack after elements are popped:')
print(stack)
if(len(stack)==0):
  print("Stack is empty\n")
else:
    print("Stack is not empty\n")

#queue
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("Lenght ",len(queue))
print("Top Element",queue[0])
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("Queue after removing elements")
print(queue)
if(len(queue)==0):
  print("Queue is empty\n")
else:
    print("Queue is not empty\n")

#binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2 #floor value
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 4
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

