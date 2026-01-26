from .models import Company

def site_context_processors(request):
    try:
        company_info = Company.objects.first()
    except Company.DoesNotExist:
        company_info = None

    return {
        'company_info': company_info,
    }