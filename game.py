name = input("이름을 입력하세요!: ")
print(name, "님 반갑습니다. {0}으로 테트리스 게임을 시작 합니다.".format(name))
print("1. 오른쪽 2. 왼쪽 3. 회전")
num = int(input("선택:"))
if num == 1:
    print("오른쪽으로 이동")
elif num == 2:
    print("왼쪽으로 이동")
elif num == 3:
    print("회전 기능")
else :
    print("게임 오버 종료")