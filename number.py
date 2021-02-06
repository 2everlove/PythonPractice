from math import *
print(abs(-5)) #5
print(pow(4,2)) #4^2=16
print(max(5, 12)) #12
print(min(5, 12)) #5
print(round(3.14)) #3


print(floor(4.99)) #4
print(sqrt(16)) #제곱근 4

from random import *
print(random()) #0.0 <= x <1.0
print(random()*10)
print(int(random()*10)) #0 <= x < 10
print(int(random()*10)+1) #1 <= x <= 10

print(int(random()*45)+1) #1<= x <=45

print(randrange(1, 46)) # 1<= x <=45
print(randrange(1, 46)) # 1<= x <=45
print(randrange(1, 46)) # 1<= x <=45
print(randrange(1, 46)) # 1<= x <=45
print(randrange(1, 46)) # 1<= x <=45
print(randrange(1, 46)) # 1<= x <=45

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임날짜는 매월 "+str(date)+"일로 선정되었습니다.")