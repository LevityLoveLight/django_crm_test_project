from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import UserUpdateForm


@login_required()
def index(request):
    template = 'users/index.html'
    users_list = User.objects.all()
    print(users_list)
    context = {
        'users_obj': users_list,
    }
    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, template, context)
