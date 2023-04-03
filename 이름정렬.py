a = []
Name = 0
RPT = 0

Name = int(input("몇명으로 하실건가요?'숫자로 입력해주세요! "))

while RPT < Name:
    x = input("이름을 입력하세요 ")
    a.append(x)
    RPT = RPT + 1
    if RPT == Name:
        a.sort()
        print(a)
    
