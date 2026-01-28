from .models import Profile

def users_context_processors(request):
    user_profile = None

    if request.user.is_authenticated:
        try:
            user_profile = request.user.profile
        except Profile.DoesNotExist:
            user_profile = None

    return {
        'user_profile': user_profile,
    }
