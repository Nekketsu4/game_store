from rest_framework import serializers

from .models import Games, Reviews, Activasion, Genre


class FilterReviewSerializer(serializers.ListSerializer):
    """Отображаем только родителей"""
    
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)



class RecursiveSerialzer(serializers.Serializer):
    """Выводим вложенные данные"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data



class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавляем отзыв"""
    # game = serializers.SlugRelatedField(slug_field='title', read_only=True)


    class Meta:
        model = Reviews
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    """Добавляем отзыв"""

    children = RecursiveSerialzer(many=True)


    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Reviews
        fields = ('name', 'message', 'children')



class ActivasionListSerializer(serializers.ModelSerializer):
    """Сериализация списка способов активации игр"""

    class Meta:
        model = Activasion
        fields = ('id', 'title', 'poster')



class ActivasionDetailSerializer(serializers.ModelSerializer):
    """Сериализация отдлельно каждого
     из способов активации игр"""

    class Meta:
        model = Activasion
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):
    """Сериализация списка жанров"""

    class Meta:
        model = Genre
        fields = ('title', 'url')


class GamesListSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Games
        fields = ('id', 'title', 'genre', 'main_image', 'price', 'url')



class GamesDetailSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(slug_field='title', read_only=True)
    localozation = serializers.CharField(source='get_localozation_display', read_only=True)
    activasion = ActivasionListSerializer(read_only=True)
    review = ReviewSerializer(many=True)


    class Meta:
        model = Games
        fields = '__all__'


