
Math = int(input("수학성적을 입력하세요"))
KiN = int(input("국어성적을 입력하세요"))
EnG = int(input("영어성적을 입력하세요"))
SoC = int(input("사회성적을 입력하세요"))
Sic = int(input("과학성적을 입력하세요"))

Sub = {
    "수학" : Math
    ,"국어" : KiN
    ,"엉어" : EnG
    ,"사회" : SoC
    ,"과학" : Sic
}
AVR = (Math + KiN + EnG + SoC + Sic)/5
print(f"평균 = {AVR}")

def Stu(a, c):
    if a == Math and c == "수학":
        if 90 <= Math <= 100 :
            print("수학공부는 이대로 쭉 가시면 됩니다!")
        elif 80 <= Math < 90:
            print("심화문제를 조금 풀어볼까요?")
        elif 70 <= Math < 80:
            print("개념을 다시한번 잡아봅시다!")
        elif 60 <= Math < 70:
            print("문제를 조금더 풀어볼까요?")
        elif 50 <= Math < 60:
            print("선생님이 말씀하신 내용을 필기해봅시다!")
        else :
            print("수업을 열심히 들어보셔야 합니다!")
    elif a == KiN and c == "국어":
        if 90 <= KiN <= 100 :
            print("국어공부는 이대로 쭉 가시면 됩니다!")
        elif 80 <= KiN < 90:
            print("교과서 내용을 정리하여 노트해 봅시다!")
        elif 70 <= KiN < 80:
            print("교과서에 나오는 책의 내용을 이해하며 읽어볼까요?")
        elif 60 <= KiN < 70:
            print("어휘력을 조금더 키워봅시다!")
        elif 50 <= KiN < 60:
            print("선생님이 말씀하신 내용을 필기해봅시다!")
        else :
            print("수업을 열심히 들어보셔야 합니다!")
    elif a == EnG and c == "영어":
        if 90 <= EnG <= 100 :
            print("영어공부는 이대로 쭉 가시면 됩니다!")
        elif 80 <= EnG < 90:
            print("심화 유형 문제를 조금 풀어볼까요?")
        elif 70 <= EnG < 80:
            print("문법을 다시한번 잡아봅시다!")
        elif 60 <= EnG < 70:
            print("숙어/ 단어를 더 외워봅시다!")
        elif 50 <= EnG < 60:
            print("선생님이 말씀하신 내용을 필기해봅시다!")
        else :
            print("수업을 열심히 들어보셔야 합니다!")
    elif a == SoC and c == "사회":
        if 90 <= SoC <= 100 :
            print("사회공부는 이대로 쭉 가시면 됩니다!")
        elif 80 <= SoC < 90:
            print("문제를 조금 풀어볼까요?")
        elif 70 <= SoC < 80:
            print("내용을 다시한번 암기해봅시다!")
        elif 60 <= SoC < 70:
            print("선생님이 말씀하신 내용을 필기해 봅시다!")
        elif 50 <= SoC < 60:
            print("교과서를 열심히 읽어봅시다!")
        else :
            print("수업을 열심히 들어보셔야 합니다!")
    elif a == Sic and c == "과학":
        if 90 <= Sic <= 100 :
            print("과학공부는 이대로 쭉 가시면 됩니다!")
        elif 80 <= Sic < 90:
            print("유형별 심화 문제를 조금 풀어볼까요?")
        elif 70 <= Sic < 80:
            print("원리를 다시한번 잡아봅시다!")
        elif 60 <= Sic < 70:
            print("과학 내용들을 검색하며 이해해 봅시다!")
        elif 50 <= Sic < 60:
            print("선생님이 말씀하신 내용을 필기해봅시다!")
        else :
            print("수업을 열심히 들어보셔야 합니다!")
    else:
        print("등록되어있지 않은 과목입니다")

b = str(input("어떤과목을 코칭할까요?"))


Stu(Sub[b], b)
