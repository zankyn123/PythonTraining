def printTitle(value: str):
    print("\n\n\n" + "➢➢➢➢➢➢➢➢➢➢➢" + value)

# Strings
stringValue = "Something STRING1 🪭 hihi"
# Methods
printTitle("String methods")
# https://docs.python.org/3/library/stdtypes.html#
print(stringValue.capitalize())
print(stringValue.casefold())
print(stringValue.count("S"))
print(stringValue.islower())
print(stringValue.title())
print(stringValue.encode())
print(stringValue.endswith(("asdasd", "hihi", "hehe")))
stringValueFormat = "Something {}"
print(stringValueFormat.format("hihi")) # replace {} sign to "hihi"

printTitle("Escaping string")
print("NewLine\n")
print("Escaping \\n")
print(r"Escaping \n") # the quote

# keep " / '
print('Escaping "value"')
print("Escaping 'value'")

# Slicing
printTitle("Slicing")
print(stringValue[1])
print(stringValue[:2])
print(stringValue[1:]) # remove first
print(stringValue[4:5])
print(stringValue[-1]) # get last
print(stringValue[-4:]) 
print(stringValue[:-1]) # remove last
print(stringValue[1:-1]) # ignore first and last
# Interate string
printTitle("Interate string")
for i in stringValue[1:-1]:
    print(i)

printTitle("Concate")
print(stringValue * 2) # Duplicate stringValue
stringValue2 = "Something String2"
print(stringValue + " " + stringValue2)

# formatted
print("toi ten la %s, nam nay toi %i tuoi" % ("Hung", 26))

# IndexError
printTitle("Index error")
print(stringValue[30])