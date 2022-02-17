import random

com = random.randint(0,100)

print('0~100까지의 숫자를 입력하시오.')
count = 0
while True:
    count = count + 1

    print("{0} 번째 도전!!".format(count))
    유저 = int(input("당신의 선택은???"))

    print (유저)

    if 유저 > com:
        print('정담보다 크네요')

    elif 유저 < com:
        print('정답보다 작네요')

    else:
        print('정답!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        break
