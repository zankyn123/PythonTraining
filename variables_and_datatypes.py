"""Learning data types and variables in Python"""

print("#### Variables")
# 1. Variables (biến)
# Được sử dụng để chứa dữ liệu
# Khai báo biến xác định kiểu dữ liệu hoặc không xác định kiểu dữ liệu
# Example:
a = 1
b = "b"
c = False
print(a,b,c)
print("\n")

a2 = int(2)
b2 = str("b2")
c2 = bool(True)
print(a2,b2,c2)
print("\n")

a3,b3,c3 = 1,2,3
print(a3, b3, c3)
print("\n")
a4 = b4 = c4 = 5
print(a4, b4, c4)
print("\n")

print(type(a4))
print("\n")



def plus():
    print(a3 + b3, " \n")

plus()


print("#### Data types")
# 2. Data Types (Kiểu dữ liệu)
# Số: int, float, comple
a = 1 # int
b = 1.2 # float
c = complex(3 + 4j) # complex

print(a, b, c)
print("\n")

# Danh sach: list, dict, set, frozenset, range, tuple
a = list((1,2,3,4)) # array
a = [1,2,3,4] # array
b = set((1,2,3,1)) # set
c = dict(value=3, value2 = 3) # dict
d = tuple((1,2,3,4)) # tupple


# kieu chu: str

a = "text"
a = str("text")

