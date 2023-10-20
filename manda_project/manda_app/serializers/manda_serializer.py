from rest_framework import serializers
from ..models import MandaMain, MandaSub, MandaContent

class MandaMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandaMain
        fields = ('id', 'user', 'main_title')

    def validate_main_title(self, value):
        if len(value) > 30:
            raise serializers.ValidationError("title은 30자 이하여야 합니다.")
        return value

class MandaSubUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sub_title = serializers.CharField()

    def validate_sub_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("세부 목표는 50글자 이하여야 합니다.")
        return value

manda_sub_update_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "sub_title": {"type": "string"}
        },
        "required": ["id", "sub_title"]
    }
}