from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse
from .models import Usuario
from .forms import SignUpForm, UpdateForm


# Profile e' o root de account
def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login_or_signup.html')

    context = {}
    context['first_name'] = request.user.first_name
    context['last_name'] = request.user.last_name
    context['social_authenticated'] = False if request.user.authenticator == 'local' else True
    context['authenticator_name'] = request.user.authenticator.title()
    context['update_ok'] = None

    if request.method == 'GET':
        context['form'] = UpdateForm(request.user)
    elif request.POST.get('update'):
        context['form'] = UpdateForm(user = request.user, request_post = request.POST)
        diff = context['form'].get_diff()
        if diff != None:
            request.user.update_user_info(diff)
            context['update_ok'] = True
        else:
            context['update_ok'] = False
    else:
        return HttpResponse(status=404)

    return render(request, 'account/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'account/login.html', {'login_erro': True})
    else:
        return render(request, 'account/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = Usuario()
            user.initialize_new_user(form.cleaned_data)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})