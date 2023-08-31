from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Screenshot, Games, Activasion, Genre, Video, Reviews


class ImageInline(admin.StackedInline):
    model = Screenshot
    extra = 1
    classes = ('collapse',)


# class VideoInline(admin.StackedInline):
#     model = Video
#     fields = ('video',)
#     extra = 1
#     classes = ('collapse',)



@admin.register(Screenshot)
class ScreenShotAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url if obj.img else None} width="120" height="90">')

    get_image.short_description = 'Картинка'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'stock', 'url', 'get_image')
    list_filter = ('genre', 'stock')
    list_editable = ('stock',)
    search_fields = ('title', 'genre__title')
    inlines = [ImageInline]
    save_on_top = True


    fieldsets = (
        (None, {
            'fields': ('title', 'main_image', 'publisher', 'developer', 'genre', 'publicated', 'localozation', 'activasion', 'age_limit', 'price', 'stock', 'url')
        }),
        ('Общие сведения о продукте', {
            'classes': ('collapse', ),
            'fields': ('description', 'features', 'purchase', 'requirements'),
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url if obj.main_image else None} width="100" height="150">')

    get_image.short_description = 'Постер'





@admin.register(Activasion)
class AdminActivasion(admin.ModelAdmin):
    list_display = ('title', 'url', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="120" height="60">')

    get_image.short_description = 'Постер'

@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('title', 'url')



@admin.register(Reviews)
class AdminReview(admin.ModelAdmin):
    list_display = ('name', 'email', 'game')


admin.site.site_title = 'Административная панель'
admin.site.site_header = 'Административная панель'


