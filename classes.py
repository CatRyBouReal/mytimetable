class Subject:
    def __init__(self, name: str, teacher: str, room: str) -> None:
        self.name = name
        self.teacher = teacher
        self.room = room


class Day:
    def __init__(self, name: str, subjects: list[Subject]) -> None:
        self.name = name
        self.subjects = subjects
