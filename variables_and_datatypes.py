"""Learning data types and variables in Python"""

print("#### Variables")
# 1. Variables (biến)
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
# 1. String
# 2. Int
# 3. Float
# 4. Array
#   4.1 List
#   4.2 Set
#   4.3 Tuple
#   4.4 Dictionary
# 5. Boolean


# str(String)
a = "text"
a = str("text")
a = 'text'

# Numberic: int, float, complex
a = 1 # int
b = 1.0 # float
c = complex(3 + 4j) # complex

# Arrays
# init list
a = list([1,2,3,4]) # cach 1
a = list((1,2,3,4)) # cach 2
a = [1,2,3,4] # cach 3
a = ["python", 1, True, 2.756] # mixed list

# init set
b = set((1,2,3,4)) # cach 1
print(type(b))
b = set([1,2,3,4]) # cach 2
print(type(b))
b = {1, 2, 3, 4} # cach 3
print(type(b))
print

# init dict
# Key-value pari
c = dict(key1='cach1', value2 = 3) # cach 1
print('test dict key1 = ', c["key1"])
c = {'cach2':1} # cach 2
print('test dict key1 = ', c["cach2"])



# init tuple
d = tuple([1,2,3,4]) # cach 1
d = tuple((1,2,3,4)) # cach 2
d = (1,2,3,4) # cach 3
# với cách 3 nếu khởi tạo d = (1) thì type(d) = int. Nhưng nếu muốn khởi tạo 1 tuple với 1 element thì thêm dấu phẩy
# d = (1,)
d = (1)
print('Tuple wrong init ', type(d))
d = (1,)
print('Tuple correct init ', type(d))