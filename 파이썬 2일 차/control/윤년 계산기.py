#현재 날짜 입력 받기
years = int(input("윤년 유무를 알고 싶은 년도를 적어주세요.\n"))

if years % 400 == 0:
    print("본 년도는 400으로 정확하게 나눠져서 윤년입니다.")
elif years % 100 == 0:
    print("본 년도는 100으로 정확하게 나눠져서 윤년이 아닙니다.")
elif years % 4 == 0:
    print("본 년도는 4로 정확하게 나눠져서 윤년입니다.")
else:
    print("본 년도는 윤년이 아닙니다.")
