from collections import Counter
from collections import defaultdict
from collections import deque

print("COUNTER EXAMPLE")
print("----------------")

data = [
    "python",
    "linux",
    "python",
    "cloud",
    "python"
]

result = Counter(data)

print(result)

print("\nDEFAULTDICT EXAMPLE")
print("----------------")

d = defaultdict(int)

d["python"] += 1
d["cloud"] += 1

print(d)

print("\nDEQUE EXAMPLE")
print("----------------")

queue = deque([1, 2, 3])

queue.appendleft(0)

print(queue)