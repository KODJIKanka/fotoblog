from django.contrib import admin
from blog.models import Category, Post

admin.site.site_header = "sana-blog"
admin.site.site_title = "sana"
admin.site.index_title = "Manageur"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at','category')
    search_fields = ('title',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


