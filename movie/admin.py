from django.contrib import admin
from .models import Movie, Review


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'user', 'movie', 'watch_again')
    list_filter = ('text', 'date', 'user', 'movie', 'watch_again')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
