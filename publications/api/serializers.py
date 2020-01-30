from rest_framework import serializers

from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id',
            'title',
            'content',
            'author',
            'category',
            'created_at',
            'published_at'
        ]
