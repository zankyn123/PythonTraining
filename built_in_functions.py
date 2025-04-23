# Cho người dùng nhập và trả về dữ liệu đã nhập
print("i")
userInput = input("input something ")
print(userInput)
# Địa chỉ vùng nhớ, có thể có nhiều biến cùng trỏ đến 1 địa chỉ 
a = 1
id(a)
# Lấy kiểu dữ liệu
type(a)


# keyword with
"""
with

Simplifies Resource Management : with statement ensures that resources are properly acquired and released, reducing the likelihood of resource leaks.
Replaces Try-Except-Finally Blocks: Traditionally, resource management required try-except-finally blocks to handle exceptions and ensure proper cleanup. The with statement provides a more concise alternative.
Enhances Readability: By reducing boilerplate code, the with statement improves code readability and maintainability.

1. not using with
file = open("example.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed

2. using with
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)  # Print file content
"""