# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from djstripe.models import Subscription, Customer

class CustomUser(AbstractUser):
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL, help_text="The user's Stripe Subscription object, if it exists")
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, help_text="The user's Stripe Customer object, if it exists") 
    
    def get_subscription(self):
        return self.subscription

    def get_plan_name(self):
        subscription = self.get_subscription()
        plan_name = subscription.plan.product.name if subscription and subscription.plan else None
        return plan_name

    def has_starter_plan(self):
        return self.get_plan_name() == "Starter"

    def has_standard_plan(self):
        return self.get_plan_name() == "Standard"

    def has_premium_plan(self):
        return self.get_plan_name() == "Premium"

    def publicaciones_permitidas(self):
        if self.has_starter_plan():
            return 3
        elif self.has_standard_plan():
            return 7
        elif self.has_premium_plan():
            return float('inf')
        return 0

    def publicaciones_actuales(self):
        count = self.propiedades.count() if hasattr(self, 'propiedades') else 0
        print(f"Publicaciones actuales: {count}")
        print(f"Publicaciones permitidas: {self.publicaciones_permitidas()}")
        return count


