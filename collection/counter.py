from collections import Counter

ls = [1, 2, 2, 2, 2, 1, "a", "b", "b"]
w = "malayalam"
s = "hello world"
print(Counter(ls))
print(Counter(w))
print(Counter(s))

# most common
print(list(Counter(ls).most_common(3)))
print(list(Counter(w).most_common(2)))
print(list(Counter(s).most_common()))

# elements
print(list(Counter(ls).elements()))
print(list(Counter(w).elements()))
print(list(Counter(s).elements()))

# subtract
d = {2:1}
x=Counter(ls)
x.subtract(d)
print(x)

#total
z=Counter(ls)
print(z.total())

#items
print(Counter(ls).items())