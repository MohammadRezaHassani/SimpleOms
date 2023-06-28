from Entity import Entity
from Lib.DataBase import DataBase


class Variant(Entity):

    def __init__(self):
        self.product_id = None
        self.price = 0
        self.number_in_stock = 0

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_product_id(self):
        return self.product_id

    def set_number_in_stock(self, number):
        self.number_in_stock = number

    def get_number_in_stock(self):
        return self.number_in_stock

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def target_data_base(self) -> DataBase:
        pass

    def serialize(self) -> dict:
        pass
