from django.apps import AppConfig


class CustomerConfig(AppConfig):
    name = 'Customer'

    def ready(self):
        import Customer.signals
