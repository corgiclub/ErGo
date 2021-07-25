from pydantic import BaseSettings


# todo 这玩意儿还不会用

class Liver(BaseSettings):

    liver: str = None
    room_id: int = None
    is_living: bool = None

    def __init__(self, liver, room_id, is_living):
        super(Liver).__init__()
        self.liver = liver
        self.room_id = room_id
        self.is_living = is_living


class Config(BaseSettings):

    auto_detect = True
    livers = [
        Liver(liver="空调Official", room_id=22406876, is_living=False),

    ]

