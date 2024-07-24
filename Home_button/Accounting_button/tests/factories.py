# Accounting_button/tests/factories.py
import factory
from Accounting_button.models import ExecutorPosition

class ExecutorPositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExecutorPosition

    position = factory.Faker('job')
    comment = factory.Faker('sentence')
