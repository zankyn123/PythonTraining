

listValue = [1,2,3,4,5]

# Methods
listValue.append(6)
listClear = [1,2,3,4,5,6]
listClear.clear()
listCopy = listValue.copy() # copy value not reference
listCopy.clear() # remove all
print(listValue)
print(listCopy)

listValue.extend([1,2,3,4]) # append array

listValue.insert(0, 0) # index + value
print(listValue)

print(listValue.pop()) # remove something with index and return value
listValue.remove(4) # remove something with value
print(listValue)


# Slicing
print(listValue[0:-1:2]) # from index 0 -> lastindex - 1 with step is 2
