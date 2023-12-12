from collections import namedtuple

x = namedtuple("student", ["name", "age"])
s = x("arun", 16)
print(s)
print(s._asdict())
print(x._make(["amal", 40]))
d = {"name": "abc", "age": 40}
print(x(**d))
