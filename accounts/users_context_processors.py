from .models import Profile

def users_context_processors(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = None

    return {
        'user_profile': user_profile,
    }