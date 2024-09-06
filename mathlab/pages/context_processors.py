from .models import SiteSettings


def site_settings(request):
    settings = SiteSettings.objects.filter()
    return {'site_settings': settings.all()}
