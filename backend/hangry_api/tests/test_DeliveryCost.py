from api.controllers import Delivery
from django_mock_queries.query import MockModel, MockSet


def test_lots_of_items():
    order = MockSet()
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))

    assert Delivery.calculate(order, distance=6) == 7.5


def test_middle_of_the_road_items():
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))

    assert Delivery.calculate(order, distance=4) == 5


def test_default_delivery_fee():
    order = MockSet()
    order.add(MockModel(quantity=3))
    order.add(MockModel(quantity=1))

    assert Delivery.calculate(order, distance=2) == 3.5
