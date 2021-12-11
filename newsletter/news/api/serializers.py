from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    headline = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    city = serializers.CharField()
    pub_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        # validated_data is an dictonary so we need to open key value pairs with 2 asterix
        return Article.objects.create(**validated_data)

    # we send object to client in update so we need to take that object
    # will ne updated as an argument (instance)
    def update(self, instance, validated_data):
        # we don't need to deal with id, created_at and updated_At
        # because our db is already handling with this field
        # so we don't take that field 
        instance.author = validated_data.get('author', instance.author)
        instance.headline = validated_data.get('headline', instance.headline)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.city = validated_data.get('city', instance.city)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance