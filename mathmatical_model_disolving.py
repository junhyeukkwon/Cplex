# 파일 열기
with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda s : s.strip('\n'), lines))

print(lines)
# '' 지우기
remove_element = ''
lines = [i for i in lines if i not in remove_element]
print(lines)

# 변수 초기화
I = int(lines[0])
Pi = int(lines[1])
M = 9999

# Oip 파싱
Oip = []
for i in range(2, 2 + Pi):
    Oip.append(list(map(int, lines[i].split())))

# Qikk_prime 파싱
Qikk_prime_start = 3 + Pi + 1
Qikk_prime = []
for i in range(Qikk_prime_start, Qikk_prime_start + I):
    Qikk_prime.append(list(map(int, lines[i].split())))

# tipj_start = Qikk_prime_start + Pi +2
# temp = []
# for i in range(tipj_start , tipj_start+I*Pi):
#     a = list(map(int,lines[i].split()))
#     temp.append(a)
# temp = [a for a in temp if a]
# tipj = []
# for i in range(0, len(temp), 3):
#     sublist = temp[i:i+3]
#     tipj.append(sublist)


temp = []
for i in range(11,13+I*Pi):
    a = list(map(int,lines[i].split()))
    temp.append(a)
temp = [a for a in temp if a]
tipj = []
for i in range(0, len(temp), 3):
    sublist = temp[i:i+3]
    tipj.append(sublist)

print("I =", I)
print("P =", Pi)
print("Oip =", Oip)
print("Qikk_prime =", Qikk_prime)
print("tipj =", tipj)


#입력파일 start
import copy
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
f = open(f'LP_file_{timestr}.lp', 'w')

print('Objective Function', file=f, end='\n\n')
print('Minimize Cmax', file=f, end='\n\n')
print('Subject to', file=f, end='\n\n')

#tipj, Qikk_prime value_mathing
for i in range(1,I+1):
    for j in range(1, Pi+1):
        for k in Oip[j-1]:
            print(f'T({i},{j},{k}) = {tipj[i-1][j-1][Oip[j-1].index(k)]}', file=f)
print('\n', file=f, end='')

for i in range(1,I+1):
    #확장성 필요
    for k in range(1,3):
        if k==1:
            print(f'Q({i},{k},{k+1}) = {Qikk_prime[i-1][k-1]}', file=f)
            print(f'Q({i},{k},{k+2}) = {Qikk_prime[i-1][k]+tipj[i-1][0][1]}', file=f)
print('\n', file=f, end='')
# Define the constraints

# Constraint (1)
for i in range(I):
    summation = ""
    for p in range(Pi):
        summation += f"Z({i+1},{p+1})+"
    summation = summation[:-1] + "=1"
    print(summation, file=f)
print('\n', file=f, end='')

# Constarint (2)
for i in range(I):
    for p in range(Pi):
        for j in range(len(Oip[p])):
            print(f"X({i + 1},{p + 1},{Oip[p][j]})-Z({i + 1},{p + 1})=0", file=f)
print('\n', file=f, end='')

# Constraint (3)
for i in range(1,I+1):
    for p in range(1,Pi+1):
        for j in Oip[p-1]:
            print(f"S({i},{p},{j})+C({i},{p},{j})-{M}X({i},{p},{j})<=0", file=f)
print('\n', file=f, end='')

# Constarint (4)

for i in range(1,I+1):
    for p in range(1,Pi+1):
        for j in Oip[p-1]:
            print(f"S({i},{p},{j})+T({i},{p},{j})-C({i},{p},{j})+{M}X({i},{p},{j})<={M}", file=f)
print('\n', file=f, end='')

#Constraint (5)
# for i in range(1,I+1):
#         for i_prime in range(1,I+1):
#             for p in range(1, Pi+1):
#                 for p_prime in range(1, Pi+1):
#                     for j in Oip[p-1]:
#                         for j_prime in Oip[p-1]:
#                             if i != i_prime:
#                                 if j_prime != 100:
#                                     print(f"S({i},{p},{j})+{M}Y({i},{p},{j},{i_prime},{p_prime},{j_prime})-C({i_prime},{p_prime},{j_prime})>=0", file=f)
# print('\n', file=f, end='')
Number = []
for chk in range(1,I+1):
    Number.append(chk)

for i in range(1, I+1):
    Number_chk = copy.deepcopy(Number)
    Number_chk.remove(i)
    for p in range(1,Pi+1):
        for j in Oip[p-1]:
            for n in range(len(Number_chk)):
                for p1 in range(1,Pi+1):
                    for j1 in Oip[p1-1]:
                        if j != 100 and j1 != 100:
                            if j1 == j:
                                print(f"S({i},{p},{j})+9999Y({i},{p},{j},{Number_chk[n]},{p1},{j1})-C({Number_chk[n]},{p1},{j1})>=0", file=f)
print('\n', file=f, end='')

#Constraint (6)
# for i in range(1,I+1):
#         for i_prime in range(1,I+1):
#             for p in range(1, Pi+1):
#                 for p_prime in range(1, Pi+1):
#                     for j in Oip[p-1]:
#                         for j_prime in Oip[p-1]:
#                             if i != i_prime:
#                                 if j_prime != 100:
#                                     print(f"S({i_prime},{p_prime},{j_prime})-{M}Y({i},{p},{j},{i_prime},{p_prime},{j_prime})-C({i},{p},{j})>=-{M}", file=f)
# print('\n', file=f, end='')

# Constraint (6)
Number_1 = []
for chk in range(1,I+1):
    Number_1.append(chk)

for i in range(1, I+1):
    Number_chk_1 = copy.deepcopy(Number_1)
    Number_chk_1.remove(i)
    for p in range(1,Pi+1):
        for j in Oip[p-1]:
            for n in range(len(Number_chk_1)):
                for p1 in range(1,Pi+1):
                    for j1 in Oip[p1-1]:
                        if j != 100 and j1 != 100:
                            if j1 == j:
                                print(f"S({Number_chk[n]},{p1},{j1})-9999Y({i},{p},{j},{Number_chk[n]},{p1},{j1})-C({i},{p},{j})>=-{M}", file=f)
print('\n', file=f, end='')

#Constraint (7)
for i in range(1, I+1):
        for p in range(1, Pi+1):
            for j in Oip[p-1]:
                if j != 1:
                    print(f"S({i},{p},{j})-C({i},{p},{Oip[p-1][(Oip[p-1].index(j))-1]})>=0", file=f)
print('\n', file=f, end='')

#Constraint (8)
for i in range(I):
    for k_prime in range(2,Pi+1):
        print(f'S({i+1},1,{k_prime})-C({i+1},1,1)-Q({i+1},1,{k_prime})<=0', file=f)
print('\n', file=f, end='')

#Constraint (9)
for i in range(I):
    for p in range(Pi):
        lip = Oip[i][-1]
        print(f"Cmax-C({i+1},{p+1},{lip})>=0", file=f)
print('\n', file=f, end='')

#Constraint (10)
for i in range(I):
    for p in range(Pi):
        for j in Oip[p]:
            print(f"S({i+1},{p+1},{j})>=0", file=f)
            
for i in range(I):
    for p in range(Pi):
        for j in Oip[p]:
            print(f"C({i+1},{p+1},{j})>=0", file=f)

for i in range(I):
    print(f"C({i+1})>=0", file=f)
print('\n', file=f, end='')

#Constraint (11)
print('BINARY','\n', file=f)
#variable Z
for i in range(I):
    for p in range(Pi):
        print(f'Z({i+1},{p+1})', file=f)
print('\n', file=f, end='')

#variable X
for i in range(1,I+1):
    for p in range(1,Pi+1):
        for j in range(len(Oip[p-1])):
            print(f'X({i},{p},{Oip[p-1][j]})', file=f)
print('\n', file=f, end='')

#variable Y
# for i in range(1,I+1):
#     for i_prime in range(1, I+1):
#         for p in range(1, Pi+1):
#             for p_prime in range(1, Pi+1):
#                 for j in Oip[p-1]:
#                     for j_prime in Oip[p-1]:
#                         if i != i_prime:
#                             if j_prime != 100:
#                                 print(f"Y({i},{p},{j},{i_prime},{p_prime},{j_prime})", file=f)
#variable Y
temp2 = []
for chk in range(1,I+1):
    temp2.append(chk)

for i in range(1, I+1):
    Number_chk_2 = copy.deepcopy(temp2)
    Number_chk_2.remove(i)
    for p in range(1,Pi+1):
        for j in Oip[p-1]:
            for n in range(len(Number_chk_2)):
                for p1 in range(1,Pi+1):
                    for j1 in Oip[p1-1]:
                        if j != 100 and j1 != 100:
                            if j1 == j:
                                print(f"Y({i},{p},{j},{Number_chk_2[n]},{p1},{j1})", file=f)
                            
            print('\n', file=f, end='')
print('\n', file=f, end='')
print('END', file=f)
f.close()