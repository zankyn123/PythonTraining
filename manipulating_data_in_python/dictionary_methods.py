
db_siso = {"lop1": 34, "lop2": 30, "lop3": 25}

# print dictionary
print(db_siso)

# get list keys
print(db_siso.keys())

# get lists values
print(db_siso.values())


keys = db_siso.keys()

for item in keys:
    a = item.count("lop1")
    print(a)