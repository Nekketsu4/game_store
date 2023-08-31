
from datetime import date

from django.db import models
# from embed_video.fields import EmbedVideoField


class Genre(models.Model):
    title = models.CharField(max_length=200, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание',  blank=True)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'



class Activasion(models.Model):
    title = models.CharField(max_length=200, verbose_name='Площадка для активации игры')
    description = models.TextField('Описание')
    poster = models.FileField(verbose_name='Картинки активации', blank=True, upload_to='media_activasion/')
    url = models.SlugField(max_length=200, unique=True, null=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Активаторы'
        verbose_name = 'Активатор'


class Games(models.Model):
    LOCAL = (
        (None, 'Выберите вариант локализации'),
        ('1', 'Полностью на русском'),
        ('2', 'Интерфейс на русском'),
        ('3', 'Субтитры на русском'),
        ('4', 'Отсутствует'),
    )

    title = models.CharField(max_length=200, verbose_name='Название')
    main_image = models.FileField(verbose_name='Картинки', blank=True, upload_to='media/images/')
    publisher = models.CharField(max_length=200, verbose_name='Издатель')
    developer = models.CharField(max_length=200, verbose_name='Разработчик')
    genre = models.ForeignKey(Genre, verbose_name='Жанр', related_name='games_genre', on_delete=models.PROTECT)
    publicated = models.DateField(verbose_name='Дата выхода', default=date.today)
    localozation = models.CharField(max_length=200, verbose_name='Локализация', choices=LOCAL, blank=True)
    activasion = models.ForeignKey(Activasion, verbose_name='Способ активации', on_delete=models.PROTECT, null=True)
    age_limit = models.PositiveSmallIntegerField(verbose_name='Возрастной рейтинг', default=18)
    stock = models.BooleanField(verbose_name='Есть в наличии?')
    description = models.TextField(verbose_name='Описание', blank=True)
    features = models.TextField(verbose_name='Особенности игры', blank=True)
    purchase = models.TextField(verbose_name='Что я приобретаю?', blank=True)
    requirements = models.TextField(verbose_name='Системные требования')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    url = models.SlugField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Игры'
        verbose_name = 'Игры'



class Screenshot(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание.', blank=True)
    img = models.FileField(verbose_name='Картинки', blank=True, upload_to='media/images/')
    game = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Скриншоты'
        verbose_name = 'Скриншот'



class Video(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    # video = EmbedVideoField(max_length=300, verbose_name='Видео', blank=True)
    game = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'



class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120, verbose_name='Имя')
    message = models.TextField(verbose_name='Сообщение', max_length=4500)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    game = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return f'{self.name} - {self.message}'


    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

