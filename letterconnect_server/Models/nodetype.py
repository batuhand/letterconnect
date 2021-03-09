import enum


class NodeType(enum.Enum):
    a1 = "a"
    b1 = "b"
    c1= "c"



a = NodeType.a1
print(a.value)