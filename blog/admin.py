from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at', 'author')
    filter_horizontal = ('tag',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Comment)
