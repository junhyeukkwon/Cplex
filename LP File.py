import copy


File_Data = open("C:/Users/user/Documents/GitHub/Cplex/Route_5_3_2_1.txt")
Data = File_Data.readline()
Tmp = []

while Data !='':
    Tmp.append(Data)
    Data = File_Data.readline()

Tmp = list(map(lambda s: s.rstrip(), Tmp))

Jobs = int(Tmp[0])
Process_Routes = int(Tmp[1])
del Tmp[0:3]

Operations = []
for i in range(Process_Routes):
    Operations.append(Tmp[i])
del Tmp[0:len(Operations)+1]

for i in range(len(Operations)):
    Operations[i] = Operations[i].split(' ')
Operations = [list(map(int, i)) for i in Operations]
print("Operation = ", Operations)


Queue_Time = []
for i in range(Jobs):
    Queue_Time.append(Tmp[i])
del Tmp[0:len(Queue_Time)+1]

for i in range(len(Queue_Time)):
    Queue_Time[i] = Queue_Time[i].split(' ')
Queue_Time = [list(map(int, i)) for i in Queue_Time]


# for i in range(Process_Routes):
#     Queue_Time.append(Tmp[i])
# del Tmp[0:len(Queue_Time)+1]

# for i in range(len(Queue_Time)):
#     Queue_Time[i] = Queue_Time[i].split(' ')
# Queue_Time = [list(map(int, i)) for i in Queue_Time]
# print("Queue_time = ", Queue_Time)

Processing_time = []
for i in range(Jobs):
    Job_Tmp = []
    for p in range(Process_Routes):
        Job_Tmp.append(Tmp[p])
    del Tmp[0:len(Job_Tmp)+1]

    for p in range(len(Job_Tmp)):
        Job_Tmp[p] = Job_Tmp[p].split(' ')
    Job_Tmp = [list(map(int, i)) for i in Job_Tmp]
    Processing_time.append(Job_Tmp)
# print(Processing_time)


for i in range(len(Processing_time)):
    Queue_Time[i][1] = Queue_Time[i][1] + Processing_time[i][0][1]
# print(Queue_Time)



#######################      DATA 불러오기       ########################


File=open("C:/Users/user/Documents/GitHub/Cplex/LP_File_"+str(100)+"_"+"_2.lp",'w')
File.write("Objective Function")
File.write("\n")
File.write("Minimize Cmax")
File.write("\n")
File.write("Subject to")
File.write("\n")
File.write("\n")


# Constraint (1)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        if p != Process_Routes:
            File.write(f"Z({i},{p}) + ")
        else:
            File.write(f"Z({i},{p})")
    File.write(" = 1")
    File.write("\n")
File.write("\n")

# Constraint (2)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("X(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" - Z(" + str(i) + "," + str(p) + ") = 0")
            File.write("\n")
File.write("\n")

# Constraint (3)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("S(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" + C(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" - 9999X(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ") <= 0")
            File.write("\n")
File.write("\n")

# Constraint (4)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("S(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" + t(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" - C(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" + 9999X(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ") <= 9999")
            File.write("\n")
File.write("\n")

for i in range(len(Processing_time)):
    for j in range(len(Processing_time[i])):
        for k in range(len(Processing_time[i][j])):
            File.write("t(" + str(i+1) + "," + str(j+1) + "," + str(Operations[j][k]) + ")")
            File.write(" = " + str(Processing_time[i][j][k]))
            File.write("\n")
File.write("\n")


#Constraint (5)
Number = []
for chk in range(1,Jobs+1):
    Number.append(chk)

for i in range(1, Jobs+1):
    Number_chk = copy.deepcopy(Number)
    Number_chk.remove(i)
    for p in range(1,Process_Routes+1):
        for j in Operations[p-1]:
            for n in range(len(Number_chk)):
                for p1 in range(1,Process_Routes+1):
                    for j1 in Operations[p1-1]:
                        if j1 == j:
                            print(f"S({i},{p},{j}) + 9999Y({i},{p},{j},{Number_chk[n]},{p1},{j1}) - C({Number_chk[n]},{p1},{j1}) >= 0", file=File)
                        if j1 == 100+j:
                            print(f"S({i},{p},{j}) + 9999Y({i},{p},{j},{Number_chk[n]},{p1},{j1}) - C({Number_chk[n]},{p1},{j1}) >= 0", file=File)
                        if 100+j1 == j:
                            print(f"S({i},{p},{j}) + 9999Y({i},{p},{j},{Number_chk[n]},{p1},{j1}) - C({Number_chk[n]},{p1},{j1}) >=0", file=File)    
print('\n', file=File, end='')


#Constraint (6)
Number_1 = []
for chk in range(1,Jobs+1):
    Number_1.append(chk)

for i in range(1, Jobs+1):
    Number_chk_1 = copy.deepcopy(Number_1)
    Number_chk_1.remove(i)
    for p in range(1,Process_Routes+1):
        for j in Operations[p-1]:
            for n in range(len(Number_chk_1)):
                for p1 in range(1,Process_Routes+1):
                    for j1 in Operations[p1-1]:
                        if j1 == j:
                            print(f"S({Number_chk_1[n]},{p1},{j1}) - 9999Y({i},{p},{j},{Number_chk_1[n]},{p1},{j1}) - C({i},{p},{j}) >= -9999", file=File)
                        if j1 == 100 + j:
                            print(f"S({Number_chk_1[n]},{p1},{j1}) - 9999Y({i},{p},{j},{Number_chk_1[n]},{p1},{j1}) - C({i},{p},{j}) >= -9999", file=File)
                        if 100 + j1 == j:
                            print(f"S({Number_chk_1[n]},{p1},{j1}) - 9999Y({i},{p},{j},{Number_chk_1[n]},{p1},{j1}) - C({i},{p},{j}) >= -9999", file=File)
print('\n', file=File, end='')


# Constraint (7)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(1,len(Operations[p-1])):
            File.write("S(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" - C(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j-1]) + ") >= 0")
            File.write("\n")
File.write("\n")

# Constraint (8)
for i in range(1,Jobs+1):
    for j in range(1,3):
        File.write("S(" + str(i) + "," + str(1) + "," + str(j+1) + ")")
        File.write(" - C(" + str(i) + "," + str(1) + "," + str(1) + ")")
        File.write(" - Q(" + str(i) + "," + str(1) + "," + str(j+1) + ") <= 0")
        File.write("\n")

File.write("\n")

for i in range(len(Queue_Time)):
    for j in range(len(Queue_Time[i])):
        File.write("Q(" + str(i+1) + "," + str(1) + "," + str(j+2) + ")")
        File.write(" = " + str(Queue_Time[i][j]))
        File.write("\n")
File.write("\n")


# Constraint (9)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        File.write("Cmax")
        File.write(" - C(" + str(i) + "," + str(p) + "," + str(Operations[p-1][-1]) + ") >= 0")
        File.write("\n")
File.write("\n")


# Constraint (10)
time = 0
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("S(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" >= " + str(time))
            File.write("\n")
File.write("\n")

for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("C(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write(" >= " + str(time))
            File.write("\n")
File.write("\n")

for i in range(1,Jobs+1):
    File.write("C(" + str(i) + ")")
    File.write(" >= " + str(time))
    File.write("\n")
File.write("\n")

File.write("BINARY")
File.write("\n")
File.write("\n")

# Constraint (11)
for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        File.write("Z(" + str(i) + "," + str(p) + ")")
        File.write("\n")
File.write("\n")

for i in range(1,Jobs+1):
    for p in range(1,Process_Routes+1):
        for j in range(len(Operations[p-1])):
            File.write("X(" + str(i) + "," + str(p) + "," + str(Operations[p-1][j]) + ")")
            File.write("\n")
File.write("\n")


Number = []
for chk in range(1,Jobs+1):
    Number.append(chk)

for i in range(1, Jobs+1):
    Number_chk = copy.deepcopy(Number)
    Number_chk.remove(i)
    for p in range(1,Process_Routes+1):
        for j in Operations[p-1]:
            for n in range(len(Number_chk)):
                for p1 in range(1,Process_Routes+1):
                    for j1 in Operations[p1-1]:
                        if j1 == j:
                            print(f"Y({i},{p},{j},{Number_chk[n]},{p1},{j1})", file=File)
                        if j1 == 100+j:
                            print(f"Y({i},{p},{j},{Number_chk[n]},{p1},{j1})", file=File)
                        if 100+j1 == j:
                            print(f"Y({i},{p},{j},{Number_chk[n]},{p1},{j1})", file=File)
print('\n', file=File, end='')

File.write("End")














