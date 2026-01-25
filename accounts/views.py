from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm, UserActivationForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False 
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            code = profile.code

            send_mail(
                'Your Registration Code',
                f'Hello {user.username}, your registration code is: {code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return render(
                request,
                'accounts/registration_success.html',
                {'email': user.email}
            )
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def activate(request):
    if request.method == 'POST':
        form = UserActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                profile = Profile.objects.get(code=code, code_used=False)
                user = profile.user
                user.is_active = True
                user.save()
                profile.code_used = True
                profile.save()
                return render(request, 'accounts/activation_success.html')
            except Profile.DoesNotExist:
                form.add_error('code', 'Invalid or already used activation code.')
    else:
        form = UserActivationForm()
    return render(request, 'accounts/activate.html', {'form': form})


