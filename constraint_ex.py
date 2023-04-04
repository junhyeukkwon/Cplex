# # 9번 제약식
# for i in range(1, n+1):
#     for p in range(1, r+1):
#         lip = Oip[i][-1]
#         C = (i, p)
#         print(f"Cmax-C{C}>=0", file=f)
# print('\n', file=f)

# # 10번 제약식
# for i in range(1, n+1):
#     for p in range(1, r+1):
#         for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
#             Operation_sequence = list(map(int,newlines[p + 3].split()))
#             S = (i, p, Operation_sequence[j-1])
#             print(f"S{S}>=0", file=f)


# for i in range(1, n+1):
#     for p in range(1, r+1):
#         for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
#             Operation_sequence = list(map(int,newlines[p + 3].split()))
#             C = (i, p, Operation_sequence[j-1])
#             print(f"C{C}>=0", file=f)

# for i in range(1, n+1):
#     C_i = (i)
#     print(f"C_i({C_i})>=0", file=f)
# print('\n', file=f)


# # 11번 제약식
# print('BINARY','\n', file=f)


# for i in range(1, n+1):
#     for p in range(1, r+1):
#         Z = (i, p)
#         print(f"Z{Z}" , file=f)
# for i in range(1, n+1):
#     for p in range(1, r+1):        
#         for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
#             Operation_sequence = list(map(int,newlines[p + 3].split()))
#             X = (i, p, Operation_sequence[j-1])
#             print(f"X{X}", file=f)

# for i in range(1, n+1):
#     for p in range(1, r+1):
#         for j in range(1, len(list(map(int,newlines[p + 3].split())))+1):
#             Operation_sequence = list(map(int,newlines[p + 3].split()))
#             for i_ in range(1, n+1):
#                 if  i != i_:
#                     for p_ in range(1, r+1):
#                         for j_ in range(1, len(list(map(int,newlines[p + 3].split())))+1):
#                             Y = (i, p, Operation_sequence[j-1], i_, p_, Operation_sequence[j_-1])
#                             print(f"Y{Y}", file=f)

# print('END', file=f)

# f.close()





# #9
# file.write("\n")
# file.write("\n")
# for i in range(1,jobn+1):
#     for j in range(1, routen+1):
#         for k in range(1,opern[j-1]+1):
#             file.write('Cmax'+'-'+'C({},{},{})'.format(i,j,k)+'>= 0')
#             file.write("\n")

# #10
# file.write("\n")
# file.write("\n")
# for i in range(1,jobn+1):
#     for j in range(1, routen+1):
#         for k in range(1,opern[j-1]+1):
#             file.write('S({},{},{})'.format(i,j,k)+'>= 0')
#             file.write("\n")
#             file.write('C({},{},{})'.format(i,j,k)+'>= 0')
#             file.write("\n")
#             file.write('C({})'.format(i)+'>= 0')
#             file.write("\n")

            
            
# #11
# file.write("\n")
# file.write("\n")
# file.write('BINARY')
# file.write("\n")
# for i in range(1,jobn+1):
#     for i1 in range(1,jobn+1):
#         for j in range(1, routen+1):
#             for j1 in range(1, routen+1):
#                 for k in range(1,opern[j-1]+1):
#                     for k1 in range(1,opern[j-1]+1):
#                         if i != i1 and j != j1 and k != k1:
#                             file.write('Z({},{})'.format(i,j))
#                             file.write("\n")
#                             file.write('X({},{},{})'.format(i,j,k))
#                             file.write("\n")
#                             file.write('Y({},{},{},{},{},{})'.format(i,j,k,i1,j1,k1))
#                             file.write("\n")


rr = open("input.txt", 'r')
line = rr.readlines()

jobn=int(line[0])
routen=int(line[1])

opern1 = list(map(int,line[3].split()))
opern2 = list(map(int,line[4].split()))
opern3 = list(map(int,line[5].split()))

file=open("first.lp",'w')

file.write('Objective Function')
file.write("\n")
file.write("\n")
file.write('Minimize Cmax')
file.write("\n")
file.write("\n")
file.write('Subject to')
file.write("\n")
file.write("\n")

        
re = []
for i in range(11,13+jobn*routen):
    a = list(map(int,line[i].split()))
    re.append(a)
re = [a for a in re if a]
pt = []
for i in range(0, len(re), 3):
    sublist = re[i:i+3]
    pt.append(sublist)

opern=[]
for i in range(3,3+jobn):
    a = list(map(int,line[i].split()))
    opern.append(a)


file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in opern[j-1]:
            file.write('T({},{},{})'.format(i,j,k)+'='+str(pt[i-1][j-1][opern[j-1].index(k)]))
            file.write("\n")
file.write("\n")



tt=[]
for i in range(7,7+jobn):
    a = list(map(int,line[i].split()))
    tt.append(a)

for i in range(1,jobn+1):
    for k in range(1,3):
        if k==1:
            file.write('Q({},{},{})'.format(i,k,k+1)+'='+str(tt[i-1][k-1]))
            file.write("\n")
            file.write('Q({},{},{})'.format(i,k,k+2)+'='+str(tt[i-1][k]))
            file.write("\n")

#1
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):

    file.write(' + '.join('Z({},{})'.format(i, j) for j in range(1, routen+1)) + '= 1')
    file.write("\n")
    
#2
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in opern[j-1]: 
            file.write('X({},{},{})'.format(i,j,k)+'-'+'Z({},{})'.format(i,j)+'= 0')
            file.write("\n")
            
#3
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in opern[j-1]:
            file.write('S({},{},{})'.format(i,j,k)+'+'+'C({},{},{})'.format(i,j,k)+'-'+'9999X({},{},{})'.format(i,j,k)+'<= 0')
            file.write("\n")
            
#4
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in opern[j-1]:
            file.write('S({},{},{})'.format(i,j,k)+'+'+'T({},{},{})'.format(i,j,k)+'-'+'C({},{},{})'.format(i,j,k)+'+'+'9999X({},{},{})'.format(i,j,k)+'<= 9999')
            file.write("\n")

#5
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for i1 in range(1,jobn+1):
        for j in range(1, routen+1):
            for j1 in range(1, routen+1):
                for k in opern[j-1]:
                    for k1 in opern[j-1]:
                        if i != i1:
                            if k1!=100:
                                file.write('S({},{},{})'.format(i,j,k)+'+'+'9999Y({},{},{},{},{},{})'.format(i,j,k,i1,j1,k1)+'-'+'C({},{},{})'.format(i1,j1,k1)+'>= 0')
                                file.write("\n")

#6
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for i1 in range(1,jobn+1):
        for j in range(1, routen+1):
            for j1 in range(1, routen+1):
                for k in opern[j-1]:
                    for k1 in opern[j-1]:
                        if i != i1:
                            if (k1!=100):
                                file.write('S({},{},{})'.format(i1,j1,k1)+'-'+'9999Y({},{},{},{},{},{})'.format(i,j,k,i1,j1,k1)+'-'+'C({},{},{})'.format(i,j,k)+'>= -9999')
                                file.write("\n")

#7
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        for k in opern[j-1]:
            if k != 1:
                file.write('S({},{},{})'.format(i,j,k)+'-'+'C({},{},{})'.format(i,j,opern[j-1][(opern[j-1].index(k))-1])+'>= 0')
                file.write("\n")

#8            
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    k=1     
    file.write('S({},{},{})'.format(i,1,k+1)+'-'+'C({},{},{})'.format(i,1,k)+'-'+'Q({},{},{})'.format(i,k,k+1)+'<= 0')
    file.write("\n")
    file.write('S({},{},{})'.format(i,1,k+2)+'-'+'C({},{},{})'.format(i,1,k)+'-'+'Q({},{},{})'.format(i,k,k+2)+'<= 0')
    file.write("\n")
            
#9
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        k=opern[j-1][-1]
        file.write('Cmax'+'-'+'C({},{},{})'.format(i,j,k)+'>= 0')
        file.write("\n")

#10
file.write("\n")
file.write("\n")
for i in range(1,jobn+1):
    file.write('C({})'.format(i)+'>= 0')
    file.write("\n")

    for j in range(1, routen+1):
        # p=opern[j-1][-1]
        # file.write('C({})'.format(i)+'>='+'C({},{},{})'.format(i,j,p))
        for k in opern[j-1]:
            
            file.write("\n")
            file.write('S({},{},{})'.format(i,j,k)+'>= 0')
            file.write("\n")
            file.write('C({},{},{})'.format(i,j,k)+'>= 0')
            file.write("\n")
            file.write("\n")

            
            
#11
file.write("\n")
file.write("\n")
file.write('BINARY')
file.write("\n")
for i in range(1,jobn+1):
    for j in range(1, routen+1):
        file.write('Z({},{})'.format(i,j))
        file.write("\n")
        for k in opern[j-1]:
            file.write('X({},{},{})'.format(i,j,k))
            file.write("\n")
            for i1 in range(1,jobn+1):
                for j1 in range(1, routen+1):
                    for k1 in opern[j-1]:
                        if i != i1:
                            if k1!=100:
                                file.write('Y({},{},{},{},{},{})'.format(i,j,k,i1,j1,k1))
                                file.write("\n")
                                            
file.write("\n")
file.write('END')