from .models import SiteSettings, Logo


def site_settings(request):
    settings = SiteSettings.objects.first()
    logo = Logo.objects.first()
    return {'site_settings': settings, 'logo': logo}
