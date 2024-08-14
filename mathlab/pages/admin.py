from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Post, Category, Contact, Screenshots, Download, Logo, Abouts


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DemoAdmin(admin.ModelAdmin):
    list_display = ('target_molecule',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',)


class ScreenshotsAdmin(admin.ModelAdmin):
    pass


class DownloadAdmin(admin.ModelAdmin):
    pass


class LogoAdmin(admin.ModelAdmin):
    pass


class AboutsAdmin(SummernoteModelAdmin):
    model = Abouts


admin.site.register(Abouts, AboutsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Screenshots, ScreenshotsAdmin)
admin.site.register(Download, DownloadAdmin)
admin.site.register(Logo, LogoAdmin)
