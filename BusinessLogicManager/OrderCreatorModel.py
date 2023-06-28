from BrokerManager.BrokerConnector import BrokerConnector
from EntityManager.Order import Order
from StockManagerModel import StockManagerModel


class OrderCreatorModel:
    # design explanation

    # this function assumes that the cart and order are created in two separate phase and two separate services
    # the order gets the cart data and after that start processing order creation so please pay attention

    def __init__(self, order: Order):
        self.order = Order()  # this is just fake entity
        self.cart_data = None

    def set_cart_data(self):
        # in the below code we should be aware of lock mechanism that to creator don't consume a single cart data
        # But we count it abstract
        cart_data = BrokerConnector.get_broker_connector(self.order, 'get_cart_data').subscribe()
        self.cart_data = cart_data

    def create_order_and_flush_in_data_store_base_on_cart_data(self):
        try:
            self.set_cart_data()
            order = self.create_order_base_on_cart(self.cart_data)
            self.order = order
            order_items = self.create_order_item_base_on_cart_data_and_order(self.cart_data, order)
            self.manage_order_stock(order, order_items)
            self.publish_order_creation_and_put_in_in_calculation_queue()

        except:
            self.publish_order_creation_error_base_on_cart_data(self.cart_data)

    def create_order_base_on_cart(self, cart) -> Order:
        pass

    def create_order_item_base_on_cart_data_and_order(self, cart_data, order) -> list:
        # returns a list of order items
        pass

    def manage_order_stock(self, order, order_items):
        stock_manager = StockManagerModel(order, order_items)
        stock_manager.calculate_stock_base_on_order_info()

    def publish_order_creation_and_put_in_in_calculation_queue(self):
        BrokerConnector.get_broker_connector(self.order, 'publish_order_creation').publish(self.order.serialize())

    def publish_order_creation_error_base_on_cart_data(self, cart_data):
        BrokerConnector.get_broker_connector(Order(), 'publish_order_creation_error').publish(self.cart_data)
