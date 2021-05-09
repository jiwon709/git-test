class MustHaveLicenseError(Exception):
    pass


class CurrentVideoCountOverFourError(Exception):
    pass


def display_video(video, user):

    try:
        video = get_video(video, user)
    except MustHaveLicenseError:
        ... # 사용권 구매 페이지로 이동
    except CurrentVideoCountOverFourError:
        ... # 메인 페이지로 이동


def get_video(video, user):
    if not user.has_licensed():
        raise MustHaveLicenseError("사용권이 있어야만 볼 수 있습니다.")
    elif user.license.current_view_count >= 4:
        raise CurrentVideoCountOverFourError("현재 시청자 수가 많습니다.")
    return get_video_contents(video)


def get_video_contents(video):
    ...
    return video