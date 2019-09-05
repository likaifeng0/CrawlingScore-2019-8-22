"""build numbers of 0000 to 999X"""

file = open('password.txt','w+')

# 0000 to 9999
for i in range(0,10000):
    if i<10:
        i = '000' + str(i) + '\n'
        file.write(i)
    elif i<100:
        i = '00' + str(i) + '\n'
        file.write(i)
    elif i<1000:
        i = '0' + str(i) + '\n'
        file.write(i)
    else:
        i = str(i) + '\n'
        file.write(i)

# 000X to 999X
for i in range(0,1000):
    if i<10:
        i = '00' + str(i) + 'X\n'
        file.write(i)
    elif i<100:
        i = '0' + str(i) + 'X\n'
        file.write(i)
    else:
        i = str(i) + 'X\n'
        file.write(i)

file.close()
print('the program has finished work of building password')
