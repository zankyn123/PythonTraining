
# Strings
stringValue = "Something STRING1"
# Methods
print("======String methods")
# https://docs.python.org/3/library/stdtypes.html#
print(stringValue.capitalize())
print(stringValue.casefold())
print(stringValue.count("S"))
print(stringValue.islower())
print(stringValue.title())
print("======Escaping string")
print("NewLine\n")
print("Escaping \\n")
print("Escaping '\n'")
print('Escaping "\n"')
print(r"Escaping \n") # the quote
# Slicing
print("======Slicing")
print(stringValue[1])
print(stringValue[:2])
print(stringValue[1:]) # remove first
print(stringValue[4:5])
print(stringValue[-1]) # get last
print(stringValue[-4:]) 
print(stringValue[:-1]) # remove last
print(stringValue[1:-1]) # ignore first and last
# Interate string
print("======Interate string")
for i in stringValue[1:-1]:
    print(i)

print("======Concate")
print(stringValue * 2) # Duplicate stringValue
stringValue2 = "Something String2"
print(stringValue + " " + stringValue2)

# IndexError
print("======Index error")
print(stringValue[30])
