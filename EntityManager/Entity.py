from Lib.DataBase import DataBase
from abc import ABC, abstractmethod


class Entity(ABC):
    # the parent which every entity in the system inherits that

    @abstractmethod
    def target_data_base(self) -> DataBase:
        # creates a database connector for the target entity and does database related actions
        pass

    @abstractmethod
    def serialize(self) -> dict:
        # this function serialize the entity data in order to put in database
        pass
