from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from opinions.models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = [
            'id',
            'category',
            'owner',
            'object_id',
            'content_type',
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Opinion.objects.all(),
                fields=['content_type', 'object_id'],
            )
        ]
        read_only_fields = ['owner']
