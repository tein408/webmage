from rest_framework import serializers
from ..models import MandaMain, MandaSub, MandaContent

class MandaMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandaMain
        fields = ('user', 'success', 'main_title')

    def validate_main_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("title은 100자 이하여야 합니다.")
        return value