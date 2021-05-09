def get_bowling_score(s):
    frame = 1  # 기본 프레임 -> 추가 점수 구하기
    stack = 0  # 프레임 추가 -> 추가 점수 구하기
    answer = 0  # 총 점수
    plus = []  # 추가 점수 구하기

    for i in range(len(s)):  # 총 점수 구하기
        append_index_to_plus(frame, i, plus, s)
        frame, stack = set_frame_and_stack(frame, i, s, stack)
        # frame, stack 이라는 변수를 동시에 업데이트하고 있어서,
        # 파이썬의 튜플이라는 자료형을 이용해서 두 가지 값을 반환해서 두 변수를 동시 업데이트

        answer += get_score(i, s) * (plus.count(i) + 1)  # 총 점수 구하

    return answer


def set_frame_and_stack(frame, i, s, stack):
    if s[i] == 'S':
        stack = 0  # 스택 초기화(프레임 구하기) -> 추가 점수 구하기
        frame += 1  # 프레임 추가(프레임 구하기) -> 추가 점수 구하기
    else:
        stack += 1  # 스택 추가(프레임 구하기) -> 추가 점수 구하기
        if stack == 2:  # 프레임 수 구하기 -> 추가 점수 구하기
            stack = 0  # 스택(프레임 구하기) 초기화 -> 추가 점수 구하기
            frame += 1  # 프레임 추가 -> 추가 점수 구하기
    return frame


def append_index_to_plus(frame, i, plus, s):
    if s[i] == 'S':
        if frame < 10:  # 추가 점수 구하기
            plus.append(i + 1)  # 추가 점수 구하기
            plus.append(i + 2)  # 추가 점수 구하기
    else:
        if s[i] == 'P':
            if frame < 10:  # 추가 점수 구하기
                plus.append(i + 1)  # 추가 점수 구하기


def get_score(i, s):
    if s[i] == 'S':
        add = 10  # 점수 구하기
    else:
        if s[i] == 'P':  # 추가 점수 구하기
            if s[i - 1] == '-':
                add = 10  # 점수 구하기
            else:
                add = 10 - int(s[i - 1])  # 점수 구하기
        elif s[i] == '-':  # 점수 구하기
            add = 0  # 점수 구하기
        else:  # 점수 구하기
            add = int(s[i])  # 점수 구하기
    return add


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300
