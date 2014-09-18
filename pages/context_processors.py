from pages.models import Branding


def branding(request):
    try:
        brand = Branding.objects.all()[0]
    except IndexError:
        brand = None
    return {
        'brand': brand,
    }
