from rest_framework import generics, permissions

from .models import Games, Activasion, Reviews, Genre
from .serializers import GamesListSerializer, GamesDetailSerializer, ReviewCreateSerializer
from .serializers import ActivasionListSerializer, ActivasionDetailSerializer
from .serializers import GenreListSerializer
from .utils import PaginateViews



class GenreListView(generics.ListAPIView):
    '''Cписок жанров игр'''

    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = None

class GamesListView(generics.ListAPIView):
    """Тут будет список игр"""

    queryset = Games.objects.all()
    serializer_class = GamesListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginateViews


    # def get(self, request):
    #     games = Games.objects.all()
    #     serializer = GamesListSerializer(games, many=True)
    #     return Response(serializer.data)


class GamesDetailView(generics.RetrieveAPIView):
    """Игры"""

    queryset = Games.objects.all()
    serializer_class = GamesDetailSerializer


    # def get(self, request, pk):
    #     games = Games.objects.get(id=pk)
    #     serilaizer = GamesDetailSerializer(games)
    #     return Response(serilaizer.data)


class ReviewDestroy(generics.DestroyAPIView):
    queryset = Reviews.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к фильму"""

    serializer_class = ReviewCreateSerializer


    # def post(self, request):
    #     review = ReviewCreateSerializer(data=request.data)
    #     if review.is_valid():
    #         review.save()
    #     return Response(status=201)



class ActivasionListView(generics.ListAPIView):
    """Выводим список активаторов"""

    queryset = Activasion.objects.all()
    serializer_class = ActivasionListSerializer



class ActivasionDetailView(generics.RetrieveAPIView):
    """Выводим отдельно активатор"""

    queryset = Activasion.objects.all()
    serializer_class = ActivasionDetailSerializer