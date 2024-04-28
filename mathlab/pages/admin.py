from django.contrib import admin

from .models import Post, Category, Contact, About, Screenshots


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DemoAdmin(admin.ModelAdmin):
    list_display = ('target_molecule',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',)


class AboutAdmin(admin.ModelAdmin):
    pass


class ScreenshotsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Screenshots, ScreenshotsAdmin)
