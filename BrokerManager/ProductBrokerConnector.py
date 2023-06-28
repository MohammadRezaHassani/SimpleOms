from Lib.Broker import Broker


class ProductBrokerConnector:

    def __init__(self, action_type):
        self.action_type = action_type

    def get_broker_connector(self):
        port, ip = self.get_broker_port_and_ip_base_on_action_type()
        broker = Broker()
        broker.set_ip(ip)
        broker.set_port(port)
        broker.connect()

    def get_broker_port_and_ip_base_on_action_type(self) -> list:
        # this can be done by reading from a config file
        return []