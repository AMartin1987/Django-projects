from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", "category")
    search_fields = ['title', 'content', 'category']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)