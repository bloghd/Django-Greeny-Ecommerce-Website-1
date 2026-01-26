from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm, UserActivationForm
from .models import Profile, UserAddress, UserPhoneNumber


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
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
            return redirect('accounts:activate', username=user.username)
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def activate(request,username):
    if request.method == 'POST':
        form = UserActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                profile = Profile.objects.get(user__username=username, code=code)
                user = profile.user
                profile.code_used = True
                user.is_active = True
                profile.save()
                user.save()
                return redirect('login')
            except Profile.DoesNotExist:
                form.add_error('code', 'Invalid activation code.')
    else:
        form = UserActivationForm()

    return render(request, 'registration/activate.html', {'form': form, 'username': username})


def profile_view(request):
    user = request.user

    profile, created = Profile.objects.get_or_create(user=user)
    addresses = UserAddress.objects.filter(user=user)
    phone_numbers = UserPhoneNumber.objects.filter(user=user)

    context = {
        'profile': profile,
        'addresses': addresses,
        'phone_numbers': phone_numbers,
    }
    return render(request, 'registration/profile.html', context)