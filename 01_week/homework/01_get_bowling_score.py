def get_bowling_score(s):
    additional_score_multiple_array = [0] * (len(s) + 2)
    answer = 0
    frame = 1
    try_count_at_frame = 0

    for i in range(len(s)):
        set_additional_score_multiple(additional_score_multiple_array, frame, i, s)
        # frame, try_count_at_frame 이라는 변수를 동시에 업데이트하고 있어서
        # 파이썬의 Tuple이라는 자료형을 이용해서 두 가지 값을 반환해서 두 변수를 업데이트를 동시에 한다.
        frame, try_count_at_frame = set_frame_and_try_count_at_frame(frame, i, s, try_count_at_frame)

        answer += get_score(i, s) * (1 + additional_score_multiple_array[i])
    print("answer is ", answer)
    return answer


def set_frame_and_try_count_at_frame(frame, i, s, try_count_at_frame):
    try_count_at_frame += 1
    if s[i] == 'S' or try_count_at_frame == 2:
        frame += 1
        try_count_at_frame = 0
    return frame


def set_additional_score_multiple(additional_score_multiple_array, frame, i, s):
    if s[i] == 'S':
        if frame < 10:
            additional_score_multiple_array[i + 1] += 1
            additional_score_multiple_array[i + 2] += 1
    elif s[i] == 'P':
        if frame < 10:
            additional_score_multiple_array[i + 1] += 1


def get_score(i, s):
    if s[i] == 'S':
        score = 10
    elif s[i] == '-':
        score = 0
    elif s[i] == 'P':
        if s[i - 1] == '-':
            score = 10
        else:
            score = 10 - int(s[i - 1])
    else:
        score = int(s[i])
    return score


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300