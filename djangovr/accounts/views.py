from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import profileForm

def signup(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        form_profile =profileForm(request.POST)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect(settings.LOGIN_URL) # 회원가입에 성공하면, LOGIN 페이지로 이동
    else:
        form_user = UserCreationForm()
        form_profile = profileForm()
    return render(request, 'accounts/signup_form.html', {
        'form_user': form_user,
        'form_profile': form_profile,
    })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
