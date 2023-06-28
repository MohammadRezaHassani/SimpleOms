from abc import ABC

from Entity import Entity
from Lib.DataBase import DataBase


class Order(Entity):

    def __init__(self):
        self.id = None
        self.total_price = 0
        self.status = None  # [ possible order_statuses]
        self.cart_id = 0
        self.user_id = 0

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_total_price(self, price):
        self.total_price = price

    def get_total_price(self):
        return self.total_price

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_cart_id(self, cart_id):
        self.cart_id = cart_id

    def get_cart_id(self):
        return self.cart_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def target_data_base(self) -> DataBase:
        pass

    def serialize(self) -> dict:
        pass


