from Entity import Entity
from Lib.DataBase import DataBase


class User(Entity):
    def __init__(self):
        self.id = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def target_data_base(self) -> DataBase:
        pass

    def serialize(self) -> dict:
        pass