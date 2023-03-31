# 9번 제약식
for i in range(1, n+1):
    for p in range(1, r+1):
        lip = Oip[i][-1]
        C = (i, p)
        print(f"Cmax-C{C}>=0", file=f)
print('\n', file=f)

# 10번 제약식
for i in range(1, n+1):
    for p in range(1, r+1):
        for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
            Operation_sequence = list(map(int,newlines[p + 3].split()))
            S = (i, p, Operation_sequence[j-1])
            print(f"S{S}>=0", file=f)


for i in range(1, n+1):
    for p in range(1, r+1):
        for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
            Operation_sequence = list(map(int,newlines[p + 3].split()))
            C = (i, p, Operation_sequence[j-1])
            print(f"C{C}>=0", file=f)

for i in range(1, n+1):
    C_i = (i)
    print(f"C_i({C_i})>=0", file=f)
print('\n', file=f)


# 11번 제약식
print('BINARY','\n', file=f)


for i in range(1, n+1):
    for p in range(1, r+1):
        Z = (i, p)
        print(f"Z{Z}" , file=f)
for i in range(1, n+1):
    for p in range(1, r+1):        
        for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
            Operation_sequence = list(map(int,newlines[p + 3].split()))
            X = (i, p, Operation_sequence[j-1])
            print(f"X{X}", file=f)

for i in range(1, n+1):
    for p in range(1, r+1):
        for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
            Operation_sequence = list(map(int,newlines[p + 3].split()))
            for i_ in range(1, n+1):
                if  i != i_:
                    for p_ in range(1, r+1):
                        for j_ in range(1, len(list(map(int,newlines[p + 3].split())))+1):
                            Y = (i, p, Operation_sequence[j-1], i_, p_, Operation_sequence[j_-1])
                            print(f"Y{Y}", file=f)

print('END', file=f)

f.close()





#9
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in range(1,opern[j-1]+1):
            file.write('Cmax'+'-'+'C({},{},{})'.format(i,j,k)+'>= 0')
            file.write("\n")

#10
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in range(1,opern[j-1]+1):
            file.write('S({},{},{})'.format(i,j,k)+'>= 0')
            file.write("\n")
            file.write('C({},{},{})'.format(i,j,k)+'>= 0')
            file.write("\n")
            file.write('C({})'.format(i)+'>= 0')
            file.write("\n")

            
            
#11
file.write("\n")
file.write("\n")
file.write('BINARY')
file.write("\n")
for i in range(1,jobn+1):
    for i1 in range(1,jobn+1):
        for j in range(1, routen+1):
            for j1 in range(1, routen+1):
                for k in range(1,opern[j-1]+1):
                    for k1 in range(1,opern[j-1]+1):
                        if i != i1 and j != j1 and k != k1:
                            file.write('Z({},{})'.format(i,j))
                            file.write("\n")
                            file.write('X({},{},{})'.format(i,j,k))
                            file.write("\n")
                            file.write('Y({},{},{},{},{},{})'.format(i,j,k,i1,j1,k1))
                            file.write("\n")