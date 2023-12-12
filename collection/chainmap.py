from collections import ChainMap


d1 = {"a": 8, "b": 6}
d2 = {"a": 8, "z": 1}
cm = ChainMap(d1,d2)
print(cm,list(cm))
