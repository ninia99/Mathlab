from django.contrib import admin

from .models import Post, Demo, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DemoAdmin(admin.ModelAdmin):
    list_display = ('target_molecule',)


admin.site.register(Post, PostAdmin)
admin.site.register(Demo, DemoAdmin)
admin.site.register(Category, CategoryAdmin)
