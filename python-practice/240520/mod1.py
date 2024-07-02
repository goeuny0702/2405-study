def add(a,b):
    return a + b

def sub(a,b):
    return a-b


# __name__은 모듈 이름을 출력한다
__name__ == "__main__":   # 모듈로 사용 시 아래 명령문은 실행하지 않도록 한다.
print(add(1,4)) # 5
print(sub(4,2)) # 2
pass