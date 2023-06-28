class Broker:
    def __init__(self):
        # the port and ip can be written from a config file
        self.port = 0
        self.ip = 0

    def set_port(self, port):
        self.port = port

    def set_ip(self, ip):
        self.ip = ip

    def connect(self):
        # connect to the proper broker and return broker Object this is an abstraction
        return self

    def publish(self, data):
        # this function publishes an event
        pass

    def subscribe(self):
        # this function gets an element from the broker
        pass
