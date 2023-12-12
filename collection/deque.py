from collections import deque


ls = [1, 2, 3, 4, 5]
ls1 = [100, 101]
dq = deque(ls)
print(dq)
dq.append(6)
print(dq)
dq.appendleft(0)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.rotate(-1)
print(dq)
dq.insert(1, 10)
print(dq)
dq.extend(ls1)
print(dq)
dq.extendleft(ls1)
print(dq)
dq.remove(101)
dq.remove(100)
print(dq)
dq.reverse()
print(dq)
