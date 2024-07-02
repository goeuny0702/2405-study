import re, usecsv, os

English = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed.It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughed at her. She realized they couldn\'t give up meat.'
## 영문을 English 객체에 저장합니다.
Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이지 말아야 한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 했습니다. 그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'
## 영문을 구글 번역기로 번역해 Korean 객체에 저장합니다

os.chdir(r'd:\goeun\python-practice1\240626')
## 번역문 csv 파일 만들기.

Korean_list = re.split(r'\.', Korean)
English_list = re.split(r'\.', English)

print(Korean_list)

total = []

for i in range(len(English_list)):
    total.append(English_list[i])