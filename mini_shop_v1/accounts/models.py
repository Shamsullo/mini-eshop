from django.db import models
from django.contrib.auth.models import AbstractUser
from store.models import Order, Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUser(AbstractUser):
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='Mobile number', 
        help_text='We need your phone number for delivery processes.')



class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def transations(self):
        transactions = Order.objects.filter(customer__user=self.user).count()
        # this is the the temporatry fix 
        transactions -= 1
        return transactions

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=MyUser)
def user_changes(sender, instance, created,*args, **kwargs):
    print("Profile created ot updated!")
    UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=MyUser)
def customer_create_or_update(sender, instance, created,*args, **kwargs):
    print("Customer is created!")
    Customer.objects.get_or_create(user=instance)
