from rest_framework import serializers

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
        read_only_fields = ['owner']
