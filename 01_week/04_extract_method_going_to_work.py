import time


def going_to_work(person, bus):
    if not time.localtime() < time.localtime("07:00"): # 출근 시간이 아니라면 멈춘다.
        return

    get_up_and_wash(person)
    get_ready_to_go_out(person)
    take_the_bus_and_go_to_the_company(bus, person)


def take_the_bus_and_go_to_the_company(bus, person):
    person.walk_to(person.near_bus_stop)  # 버스 정류장으로 걸어간다. -> 버스 타서 회사로 간다.
    while bus.location is person.near_bus_stop:  # 버스가 버스정류장까지 올때까지 -> 버스 타서 회사로 간다.
        person.wait()  # 기다린다.
    person.ride(bus)  # 버스를 탑승한다.
    if not person.type == "DISABLED" and not person.type == "NATIONAL_MERIT":  # 장애우와 국가유공자는 무료이다.
        person.pay_fee(bus)  # 버스비를 낸다.
    while bus.location is person.company_near_bus_stop:  # 회사 인근 버스정류장까지 버스가
        person.wait()  # 기다린다.
    person.walk_to(person.company)  # 그리고 회사로 걸어간다.


def get_ready_to_go_out(person):
    if person.gender == "woman":  # 여자라면 -> 외출 준비를 한다.
        person.pull_on("클로니더블자켓")  # 입는다. -> 외출 준비를 한다.
        if person.like("화장"):  # 화장면 좋아하면, -> 외출 준비를 한다.
            person.make_up()  # 화장한다. -> 외출 준비를 한다.
    elif person.gender == "man":  # 남자라면 -> 외출 준비를 한다.
        person.pull_on("맨투맨")  # 입는다. -> 외출 준비를 한다.
        person.shave()  # 면도한다. -> 외출 준비를 한다.


def get_up_and_wash(person):
    person.wake_up_from_the_bed()  # 침대에서 일어난다. -> 일어나서 씻는다.
    person.go_to_bathroom()  # 화장실에 간다. -> 일어나서 씻는다.
    person.turn_on_the_water()  # 물을 켠다. -> 일어나서 씻는다.
    person.wash_face()  # 얼굴을 씻는다. -> 일어나서 씻는다.
    if not person.already_shower_yesterday():  # 어제 샤워를 안했다면 -> 일어나서 씻는다.
        person.take_a_shower()  # 샤워를 한다. -> 일어나서 씻는다.