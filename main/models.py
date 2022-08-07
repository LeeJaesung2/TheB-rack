from django.db import models

# Create your models here.

class Bycicle_info(models.Model):
    position = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    rack_time = models.DateTimeField()


# json 형식
# {
#     "position": 2,
#     "status": 2,
#     "rack_time": "2022-08-07T09:18:02Z"
# }