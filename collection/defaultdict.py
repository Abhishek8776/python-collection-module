from collections import defaultdict


a = defaultdict(int)
print(a["x"])
a = defaultdict(str)
print(a["x"])
a = defaultdict(float)
print(a["x"])
a = defaultdict(list)
print(a["x"])
a = defaultdict(dict)
print(a["x"])

x={1:5,2:'x','y':8}
d=defaultdict(int)
for k,v in x.items():
  d[k]=v
print(d)
print(d[76])