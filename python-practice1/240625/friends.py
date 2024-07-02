# 사전작업 : friends101.txt 파일을 현재 friends.py 파일의 같은 폴더에 넣기
import os, re

print(os.getcwd())
# 여러분들의 friends.py 저장경로
os.chdir(r'D:\goeun\python-practice1\240625')

f = open('friends101.txt', 'r', encoding= 'utf-8')  # 프렌즈101 대본 파일 내용 읽기모드로 열기
script101 = f.read()
print(script101[:100])

# 첫번째 실습: 특정 등장인물의 대사만 모으기 (monica의 대사만 가져오기)
Line = re.findall(r'Monica:.+', script101)
#type(Line) -> 리스트
for item in Line[:3]:
    print(item)

# Monica의 대사만 있는 monica.txt 파일 만들기
f = open('monica.txt', 'w', encoding='utf-8')
monicaLineScript = ''
for monicaScript in Line:
    monicaLineScript += monicaScript + "\n"

f.write(monicaLineScript)
f.close()

# 두번째실습: 등장인물 리스트 만들기
# 등장인물 이름 모으기
# print(re.findall(r'[A-Z][a-z]+: ', script101))
# print('-' * 150)
# print(set(re.findall(r'[A-Z][a-z]+: ', script101)))

# 콜론과 빈공백 제거하기
listPeopleName = list(set(re.findall(r'[A-z][a-z]+: ', script101)))
character = []
for peopleName in listPeopleName:
    character.append(peopleName[:-2]) # 뒤에서 2문자 제거하고 character 리스트에 넣기
    # print(peopleName[:-2])
print(character)    


