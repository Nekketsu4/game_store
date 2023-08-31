from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('list_genres/', views.GenreListView.as_view()),
    path('list_games/', views.GamesListView.as_view()),
    path('list_games/<int:pk>/', views.GamesDetailView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path('review/<int:pk>/', views.ReviewDestroy.as_view()),
    path('activasion/', views.ActivasionListView.as_view()),
    path('activasion/<int:pk>/', views.ActivasionDetailView.as_view())
]