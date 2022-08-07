from rest_framework import serializers
from .models import Bycicle_info

class BycicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bycicle_info
        fields = ('position', 'status', 'rack_time')
        