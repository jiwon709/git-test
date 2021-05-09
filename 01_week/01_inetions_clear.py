# 사람들을 입력받은 다음 어른들(19살 보다 나이 많은) 뽑아서 반환해주고 싶습니다.
# get adults from peaple

ADULT_AGE = 19


def get_adults(people):
    adults = []
    for person in people:
        if person.age > ADULT_AGE:
            adults.append(person)
    return adults
