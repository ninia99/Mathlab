from django.contrib import admin

from .models import Category, Tag, Post, Demo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DemoAdmin(admin.ModelAdmin):
    list_display = ('target_molecule',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Demo, DemoAdmin)
