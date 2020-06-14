from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
# Create your models here.
User = settings.AUTH_USER_MODEL

def set_delete_user():
    User = get_user_model()
    return User.objects.get_or_create(username='pranav')[0]

def limit_car_choice():
    Q = models.Q
    return Q(username__icontains='pra') | Q(username__icontains='mi')

class Car(models.Model):
    # first_owner = models.OneToOneField(User,on_delete=models.CASCADE)
    # passengers = models.ManyToManyField(User)
    user = models.ForeignKey(
                            User,
                            on_delete=models.SET(set_delete_user),
                            limit_choices_to= limit_car_choice,
                            )
    updated_by = models.ForeignKey(User,related_name='car_user',null=True,blank=True,on_delete=models.CASCADE)
    # drivers = models.ManyToManyField(User)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

