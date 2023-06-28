from EntityManager.Entity import Entity
from EntityManager.Order import Order
from EntityManager.OrderItem import OrderItem
from EntityManager.Product import Product
from EntityManager.User import User
from EntityManager.Variant import Variant
from OrderBrokerConnector import OrderBrokerConnector
from OrderItemBrokerConnector import OrderItemBrokerConnector
from ProductBrokerConnector import ProductBrokerConnector
from UserBrokerConnector import UserBrokerConnector
from VariantBrokerConnector import VariantBrokerConnector


class BrokerConnector:
    # short explanation: base on the entity type and the action entity want to do the connected broker can be different

    @staticmethod
    def get_broker_connector(entity: Entity, action: str):
        if isinstance(entity, Order):
            return OrderBrokerConnector(action).get_broker_connector()
        elif isinstance(entity, OrderItem):
            return OrderItemBrokerConnector(action).get_broker_connector()
        elif isinstance(entity, Product):
            return ProductBrokerConnector(action).get_broker_connector()
        elif isinstance(entity, User):
            return UserBrokerConnector(action).get_broker_connector()
        elif isinstance(entity, Variant):
            return VariantBrokerConnector(action).get_broker_connector()

        # this can be extended base on the entity type and the action we want to do
