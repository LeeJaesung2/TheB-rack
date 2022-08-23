from django.db import models
from user.models import User

# Create your models here.

class Bycicle_info(models.Model):
    position = models.IntegerField(primary_key=True)
    status = models.IntegerField()
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