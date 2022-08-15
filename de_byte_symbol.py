de_1byte = {}
de_2byte = {}

for i in range(1114112):
    try:
        if len(chr(i).encode()) == 1:
            de_1byte[i] = chr(i)
        if len(chr(i).encode()) == 2:
            de_2byte[i] = chr(i)
    except UnicodeEncodeError:
        pass

print(de_1byte)
print(de_2byte)
print(len(de_1byte))
print(len(de_2byte))