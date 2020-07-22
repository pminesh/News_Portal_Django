from rest_framework import serializers
from .models import news

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ('title','category','subcat','details','image','date')