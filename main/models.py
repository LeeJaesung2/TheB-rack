from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Bycicle_info(models.Model):
    position = models.IntegerField(primary_key=True)
    
    STATUS_CHOICE=(
        (0,'빈 자리'),
        (1,'거치중'),
        (2,'도난'),
    )

    STATUS_SECTION = [MaxValueValidator(2),MinValueValidator(0)]

    status = models.IntegerField(validators=STATUS_SECTION, choices = STATUS_CHOICE)
    rack_time = models.DateTimeField()
    def __str__(self):
        return str(self.position)

class Brack(models.Model):
    position = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bycicle = models.ForeignKey(Bycicle_info, on_delete=models.CASCADE)
    def __str__(self):
        return self.username.username




# json 형식
# {
#     "position": 2,
#     "status": 2,
#     "rack_time": "2022-08-07T09:18:02Z"
# }