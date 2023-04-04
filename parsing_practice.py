# 파일 열기
with open("Route_5_3_2_1.txt", "r") as f:
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

print(Oip)

# Qikk_prime 파싱
Qikk_prime_start = 2 + Pi
Qikk_prime = []
for i in range(Qikk_prime_start, Qikk_prime_start + I):
    Qikk_prime.append(list(map(int, lines[i].split())))
print(Qikk_prime)

#Tipj 파싱
tipj_start = Qikk_prime_start + Pi
temp = []
for i in range(tipj_start,tipj_start+I*Pi):
    a = list(map(int,lines[i].split()))
    temp.append(a)
temp = [a for a in temp if a]
tipj = []
for i in range(0, len(temp), Pi):
    sublist = temp[i:i+3]
    tipj.append(sublist)

print(tipj)