from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, default="avatar.svg")


    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'

    @receiver(post_save, sender=User)
    def update_create_profile(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    def save_profile(self):
        self.save()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    STATIONS = (('Mwiki - 6:22 AM', 'Mwiki - 6:22 AM'),('Maji Mazuri - 6:24 AM', 'Maji Mazuri - 6:24 AM'),('Kamutini -  6:27 AM', 'Kamutini - 6:27 AM'),('Sunton - 6:30 AM','Sunton - 6:30 AM'),('Hunters - 6:33 AM', 'Hunters - 6:33 AM'))
    station = models.CharField(max_length=50, choices=STATIONS, null=True)
    date = models.DateField()
    AMOUNT = (('Ksh. 0.00','Ksh. 0.00'),('Ksh. 50.00','Ksh. 50.00'))
    amount = models.CharField(max_length=30, choices=AMOUNT, null=True,default = 'Ksh. 50.00')
    TRIPS =(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    no_of_trips = models.CharField(max_length=50, choices=TRIPS, null=True,default='1')
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return f'{self.user.username}'