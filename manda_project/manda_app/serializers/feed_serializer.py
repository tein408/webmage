from rest_framework import serializers
from django.contrib.auth.models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'