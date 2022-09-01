import factory
from faker import Faker
from django.contrib.auth import get_user_model
from store_api import models
from orders.models import Order, OrderItem, OrderPayment
from django.db.models.signals import post_save


User = get_user_model()

fake = Faker()


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email =  factory.Sequence(lambda n: 'person1{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user1_%d" % n)
    role = "CL"
    is_active = True


class StoreOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email =  factory.Sequence(lambda n: 'person{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user_%d" % n)
    is_active = True
    role = "SO"


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Store

    store_owner = factory.SubFactory(StoreOwnerFactory)
    store_name = fake.name()
    email = fake.email()
    about = fake.text()
    policy_type = 'FPBP'
    part_payment_percentage = 0
    status = 'A'


class BranchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Branch

    store = factory.SubFactory(StoreFactory)
    branch_name = fake.name()
    location = fake.city()
    street_name = fake.street_address()
    digital_address = fake.postcode()


class DesignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Design

    store_branch = factory.SubFactory(BranchFactory)
    style = factory.Sequence(lambda n: "style_%d" % n)
    description = fake.text()
    fabric_available = True
    price_with_store_fabric = fake.pydecimal(positive=True, min_value=200.00, max_value=1000.00)
    price_without_store_fabric = fake.pydecimal(positive=True, min_value=100.00, max_value=700.00)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    client = factory.SubFactory(ClientFactory)
    total_cost = fake.pydecimal(positive=True, min_value=200.00, max_value=1000.00)
    payment_status = "NP"
    store_branch = factory.SubFactory(BranchFactory)
    order_status = "R"


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    design = factory.SubFactory(DesignFactory)
    order = factory.SubFactory(OrderFactory)
    fabric_source = 'FM'
    quantity = fake.pyint()
    unit_cost = fake.pydecimal(positive=True, min_value=200.00, max_value=1000.00)
    total_item_cost = fake.pydecimal(positive=True, min_value=200.00, max_value=100000.00)


class OrderPayment(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderPayment

    order = factory.SubFactory(OrderFactory)
    amount = fake.pydecimal(positive=True, min_value=200.00, max_value=1000.00)
