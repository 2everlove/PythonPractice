sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990706-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2]) #0부터 2직전까지
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

# print("생년월일 : "+jumin[0:6]) #처음부터 6직전까지
print("생년월일 : "+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : "+jumin[7:14])
print("뒤 7자리 : "+jumin[7:])
print("뒤 7자리 (뒤에서 부터) : "+jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower()) #소문자 표기
print(python.upper()) #대문자 표기
print(python[0].isupper()) #0번째(첫번째) 글자 대문자? true
print(len(python)) #길이
print(python.replace("Python", "Java")) # "Java is Amazing"

index = python.index("n")
print(index) #5번째에 n있음
index = python.index("n", index + 1)
print(index) #첫번째 인덱스 다음의(index+1 => 1) 인덱스는 15번째에 n있음

print(python.find("Java")) #없으면 -1 반환
# print(python.index("Java")) #값이 없으므로 error

print(python.count("n")) #2

print("a"+"b")
print("a","b")

print("나는 %d살입니다" % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
apple = "Apple은 %c로 시작해요"
print(apple % apple[0])
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))


print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# v3.6이상~
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#탈출문자
print("백문이 불여일견 \n백견이 불여일타")

print('저는 "mika"입니다.')
print("저는 \"mika\"입니다.") #\" \' ""내에서 "" || ''출력가능

print("C:\\pythonWorks") #\\ ""내에서 \출력

print("Red Apple\rPine") #PineApple -> Red"공백"까지 포함해서 Pine이 덮음

print("Redd\bApple") #\b 백스페이스

print("Red\tApple") #\t tap

#quiz
url = "http://naver.com"
print(url[7:]) #naver.com
a = url[7:url.index(".")] #naver
print(a[0:3]+str(len(a))+str(a.count("e"))+"!")

my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))
print(f"{url}의 비밀번호는 {password}입니다")