점수들 = [90, 25, 67, 45, 80, 100, 54, 97, 86, 94, 23, 65, 78, 87, 65, 76, 96, 38, 98, 68, 86, 97, 56, 76, 96, 19, 91, 10, 98, 89, 56, 99, 100, 27, 60, 90, 47, 67, 84, 59 ,40, 86, 85, 49, 73, 30, 52, 92, 90]

number = 0
for 점수 in 점수들:
    number = number +1
    if 점수 >= 60:
        print ("{}번 학생은 합격 입니다.".format(number))
    else:
        print ("{}번 학생은 불합격 입니다.".format(number))

from multiprocessing.dummy import current_process
import 수학

print(수학.더하기(99348, 928645))
print(수학.곱하기(99999999698264528736458297645, 9692476597934356982))
print(수학.나누기(97324659873465927346952764957826349562397846529734659274365927346, 19))

import time

print('현재시각:', time.time())

def manyioop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')

number = int(input('숫자를 임력하세요: '))
manyioop(number)

import time

current = time.ctime()
print(current)
