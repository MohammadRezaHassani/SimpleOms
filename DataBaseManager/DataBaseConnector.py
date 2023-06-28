from Lib.DataBase import DataBase


class DataBaseConnector:

    @staticmethod
    def get_data_base_connector(database: DataBase):
        return database.connect()
