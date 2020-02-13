from rest_framework import serializers

from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    opinion_count = serializers.IntegerField(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    dislike_count = serializers.IntegerField(read_only=True)
    current_user_opinion = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publication
        fields = [
            'id',
            'title',
            'content',
            'author',
            'category',
            'created_at',
            'published_at',
            'opinion_count',
            'like_count',
            'dislike_count',
            'current_user_opinion',
        ]
