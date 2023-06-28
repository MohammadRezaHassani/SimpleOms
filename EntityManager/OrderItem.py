from Entity import Entity
from Lib.DataBase import DataBase


class OrderItem(Entity):

    def __init__(self):
        self.id = None
        self.order_id = None
        self.variant_id = None
        self.count = None
        self.price = 0

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_variant_id(self, variant_id):
        self.variant_id = variant_id

    def get_variant_id(self):
        return self.variant_id

    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_order_id(self):
        return self.order_id

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def target_data_base(self) -> DataBase:
        pass

    def serialize(self) -> dict:
        pass

