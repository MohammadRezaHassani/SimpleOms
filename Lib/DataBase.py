class DataBase:

    def __init__(self):
        # the port and ip can be written from a config file
        self.port = 0
        self.ip = 0

    def connect(self):
        # connect to the proper database and return database Object this is an abstraction
        return self

    def flush(self, data):
        # this function flushes in the database base on the data and the table name
        pass
