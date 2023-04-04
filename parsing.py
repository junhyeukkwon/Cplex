import copy


File_Data = open("C:/Users/user/Desktop/CPLEX/LP_File_Data.txt")
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
for i in range(Process_Routes):
    Queue_Time.append(Tmp[i])
del Tmp[0:len(Queue_Time)+1]

for i in range(len(Queue_Time)):
    Queue_Time[i] = Queue_Time[i].split(' ')
Queue_Time = [list(map(int, i)) for i in Queue_Time]
print("Queue_time = ", Queue_Time)


Job1_Processing_Time = []
for i in range(Process_Routes):
    Job1_Processing_Time.append(Tmp[i])
del Tmp[0:len(Job1_Processing_Time)+1]

for i in range(len(Job1_Processing_Time)):
    Job1_Processing_Time[i] = Job1_Processing_Time[i].split(' ')
Job1_Processing_Time = [list(map(int, i)) for i in Job1_Processing_Time]
print("Job1_Processing_Time = ", Job1_Processing_Time)


Job2_Processing_Time = []
for i in range(Process_Routes):
    Job2_Processing_Time.append(Tmp[i])
del Tmp[0:len(Job2_Processing_Time)+1]

for i in range(len(Job2_Processing_Time)):
    Job2_Processing_Time[i] = Job2_Processing_Time[i].split(' ')
Job2_Processing_Time = [list(map(int, i)) for i in Job2_Processing_Time]
print("Job2_Processing_Time = ", Job2_Processing_Time)


Job3_Processing_Time = []
for i in range(Process_Routes):
    Job3_Processing_Time.append(Tmp[i])
del Tmp[0:len(Job3_Processing_Time)+1]

for i in range(len(Job3_Processing_Time)):
    Job3_Processing_Time[i] = Job3_Processing_Time[i].split(' ')
Job3_Processing_Time = [list(map(int, i)) for i in Job3_Processing_Time]
print("Job3_Processing_Time = ", Job3_Processing_Time)

Processing_time = []
Processing_time.append(Job1_Processing_Time)
Processing_time.append(Job2_Processing_Time)
Processing_time.append(Job3_Processing_Time)