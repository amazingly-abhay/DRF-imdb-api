from rest_framework import serializers
from .models import WatchList,StreamingPlatform


# class WatchListSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField()
#     storyline=serializers.CharField()
#     # platform=serializers.ForeignKey(StreamingPlatform,on_delete=models.CASCADE)
#     active=serializers.BooleanField()
#     created=serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return WatchList.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchList
        fields='__all__'


class StreamingPlatformSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    about=serializers.CharField()
    website=serializers.URLField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return StreamingPlatform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website',instance.website)
        instance.save()
        return instance