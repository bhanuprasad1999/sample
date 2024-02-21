from rest_framework import serializers
from .models import *


class CodeFormaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFormater
        fields = '__all__'  # or specify the fields you want to include
