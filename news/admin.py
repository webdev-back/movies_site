from django.contrib import admin
from .models import News


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date')
    list_filter = ('headline', 'date')


admin.site.register(News, NewsAdmin)
