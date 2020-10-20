from rest_framework import serializers
from articles.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Articles
        fields = ['title', 'author', 'create_date', 'text']


