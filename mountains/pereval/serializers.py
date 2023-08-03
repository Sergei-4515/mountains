from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Users, Pereval, Images, Coords


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    data_1 = serializers.URLField(label='URL изображения 1', allow_blank=True)
    data_2 = serializers.URLField(label='URL изображения 2', allow_blank=True)

    class Meta:
        model = Images
        fields = ['data_1', 'title_1', 'data_2', 'title_2']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    images = ImagesSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time',  'user', 'coords',
                  'status', 'level', 'images']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        images_data = validated_data.pop('images')
        coords_data = validated_data.pop('coords')

        user = Users.objects.create(**user_data)
        images = Images.objects.create(**images_data)
        coords = Coords.objects.create(**coords_data)

        pereval = Pereval.objects.create(user=user, images=images, coord=coords, **validated_data)
        pereval.save()
        return pereval


