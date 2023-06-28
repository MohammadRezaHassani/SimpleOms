from OrderItemCalculatorModel import OrderItemCalculatorModel
from BrokerManager.BrokerConnector import BrokerConnector
from EntityManager.Order import Order


class OrderCalculatorModel:

    def __init__(self):
        self.order = Order()

    def get_order(self):
        order = BrokerConnector.get_broker_connector(self.order, 'get_created_orders').subscribe()
        # again pay attention that the lock mechanism should be considered  not to consume the same order twice
        self.order = order

    def calculate_order(self):
        try:
            self.get_order()
            order_item_calculator = OrderItemCalculatorModel(self.order)
            order_item_calculator.calculate_order_items_of_order()
            self.calculate_order_total_price()
        except:
            BrokerConnector.get_broker_connector(self.order, 'order_calculation_error').publish(self.order.serialize())

    def calculate_order_total_price(self):
        # this function calculates the order total price
        pass
