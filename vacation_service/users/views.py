from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from .models import User, Vacation
from .forms import UserUpdateForm, VacationUpdateForm
from .utils import vacation_per_page


@login_required
def index(request):
    template = 'users/index.html'
    vacation_cache_name = 'vacation_cache'
    vacation_cache = cache.get(vacation_cache_name)
    if vacation_cache:
        vacation_list = vacation_cache
    else:
        vacation_list = Vacation.objects.all().order_by('vacation_date_start').select_related("user")
        cache.set(vacation_cache_name, vacation_list, 30)
    context = {
        'vacation_obj': vacation_per_page(request, vacation_list),
    }
    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, template, context)


@login_required()
def vacation(request):
    template = 'users/vacation.html'
    if request.method == 'POST':
        v_form = VacationUpdateForm(request.POST)
        if v_form.is_valid():
            vacation_obj = v_form.save(commit=False)
            vacation_obj.user = request.user
            vacation_obj.save()
            return redirect('users:vacation')
    else:
        v_form = VacationUpdateForm()

    context = {
        'v_form': v_form,
    }
    return render(request, template, context)
