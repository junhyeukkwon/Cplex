# #파일 불러들기
f = open("input.txt",'r')
lines = f.readlines()
lines = list(map(lambda s : s.strip('\n'), lines))

#입력파일 start
f = open('stdout2.txt', 'w')

# # Define the problem parameters
I =  int(lines[0]) # Jobs
Pi = int(lines[1]) # Process routes
del lines[0]
del lines[0]
lines.remove('')
Oip = [] # Ordered set of operations for each job i and process route p
for i in range(Pi):
    Oip.append(list(map(int,lines[i].split())))
print(Oip)
M = 999 # A large number

print('Objective Function', file=f, end='\n\n')
print('Minimize Cmax', file=f, end='\n\n')
print('Subject to', file=f, end='\n\n')

# Define the constraints

# # Constraint (1)
for i in range(I):
    summation = ""
    for p in range(Pi):
        summation += f"Z({i+1},{p+1})+"
    summation = summation[:-1] + "= 1"
    print(summation, file=f)
print('\n', file=f, end='')

# # Constarint (2)
# #version 1
# # for i in range(1,I+1):
# #     for p in range(1,Pi+1):
# #         for j in Oip:
# #             print("X({i},{p},{j})=Z({i},{p})".format(i=i,p=p,j=j))
# #verion 2
for i in range(I):
    for p in range(Pi):
        for j in range(len(Oip[p])):
            print(f"X({i + 1},{p + 1},{Oip[p][j]}) - Z({i + 1},{p + 1}) = 0", file=f)
print('\n', file=f, end='')

# # Constraint (3)
# #version 1
# # for i in range(1,I+1):
# #     for p in range(1,Pi+1):
# #         for j in Oip:
# #             print("S({i},{p},{j}) + C({i},{p},{j}) <= {M}X({i},{p},{j})".format(i=i,p=p,j=j, M=M))
# #version 2
for i in range(I):
    for p in range(Pi):
        for j in range(len(Oip[p])):
            print(f"S({i + 1},{p + 1},{Oip[p][j]}) + C({i + 1},{p + 1},{Oip[p][j]}) - {M} * X({i + 1},{p + 1},{Oip[p][j]}) <= 0", file=f)
print('\n', file=f, end='')

# # Constarint (4)
# #version 1
# # for i in range(1,I+1):
# #     for p in range(1,Pi+1):
# #         for j in Oip:
# #             print("S({i},{p},{j}) + t({i},{p},{j}) <= C({i},{p},{j}) + {M}(1-X({i},{p},{j}))".format(i=i,p=p,j=j, M=M))
# #version 2
for i in range(I):
    for p in range(Pi):
        for j in range(len(Oip[p])):
            print(f"S({i + 1},{p + 1},{Oip[p][j]}) + t({i + 1},{p + 1},{Oip[p][j]}) - C({i + 1},{p + 1},{Oip[p][j]}) - {M} * (1 - X({i + 1},{p + 1},{Oip[p][j]})) <= 0", file=f)
print('\n', file=f, end='')

#Constraint (5)
#version 1
# for i in range(I):
#     for i_prime in range(I):
#         if i == i_prime:
#             continue
#         for p in range(Pi):
#             for p_prime in range(Pi):
#                 for j in range(len(Oip[p]) - 1):
#                     for j_prime in range(len(Oip[p_prime]) - 1):
#                         print(f"S({i + 1},{p + 1},{Oip[p][j]}) + {M} * Y({i + 1},{i_prime + 1},{p + 1},{p_prime + 1},{Oip[p][j]},{Oip[p_prime][j_prime]}) >= C({i_prime + 1},{p_prime + 1},{Oip[p_prime][j_prime]})", file=f)
# print('\n', file=f, end='')

#version 2
for i in range(I):
        for i_prime in range(I):
            if i != i_prime:
                for p in range(Pi):
                    for p_prime in range(Pi):
                        for j in Oip[i]:
                            for j_prime in Oip[i_prime]:
                                print(f"S({i+1},{p+1},{j}) + {M} * Y({i+1},{p+1},{j},{i_prime+1},{p_prime+1},{j_prime}) - C({i_prime+1},{p_prime+1},{j_prime}) >= 0", file=f)
print('\n', file=f, end='')


#Constraint (6)
for i in range(I):
    for i_prime in range(I):
        if i != i_prime:
            for p in range(Pi):
                for p_prime in range(Pi):
                    for j in Oip[i]:
                        for j_prime in Oip[i_prime]:
                            print(f"S({i_prime+1},{p_prime+1},{j_prime}) + {M} * (1 - Y({i+1},{p+1},{j},{i_prime+1},{p_prime+1},{j_prime})) - C{i+1}{p+1}{j} >= 0", file=f)
print('\n', file=f, end='')

#Constraint (7)
for i in range(I):
        for p in range(Pi):
            first_op = Oip[i][0]
            for j in range(1, len(Oip[i])):
                print(f"S({i+1},{p+1},{Oip[i][j]}) - C{i+1}{p+1}{Oip[i][j-1]} >= 0", file=f)
print('\n', file=f, end='')

#Constraint (8)
for i in range(I):
    for k_prime in range(2,Pi+1):
        print(f'S({i+1},1,{k_prime})-C({i+1},1,1)-Q({i+1},1,{k_prime}) <= 0', file=f)
print('\n', file=f, end='')

#Constraint (9)
# for i in range()
f.close()