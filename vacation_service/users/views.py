from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .forms import ProfileUpdateForm, VacationUpdateForm
from .models import Vacation
from .utils import vacation_per_page


@login_required
def index(request):
    """Функция для работы с Главной страницей"""
    template = "users/index.html"
    vacation_cache_name = "vacation_cache"
    vacation_cache = cache.get(vacation_cache_name)
    if vacation_cache:
        vacation_list = vacation_cache
    else:
        vacation_list = (
            Vacation.objects.all()
            .order_by("vacation_date_start")
            .select_related("user")
        )
        cache.set(vacation_cache_name, vacation_list, 15)
    context = {
        "vacation_obj": vacation_per_page(request, vacation_list),
    }
    return render(request, template, context)


@login_required
def profile(request):
    """Функция для работы со страницей Профиль"""
    template = "users/profile.html"
    if request.method == "POST":
        u_form = ProfileUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect("users:profile")
    else:
        u_form = ProfileUpdateForm(instance=request.user)

    context = {
        "u_form": u_form,
    }
    return render(request, template, context)


@login_required()
def vacation(request):
    """Функция для работы со страницей Добавить отпуск"""
    users_vacations = Vacation.objects.filter(user=request.user).order_by(
        "vacation_date_start"
    )
    template = "users/vacation.html"
    if request.method == "POST":
        v_form = VacationUpdateForm(request.POST)
        if v_form.is_valid():
            vacation_obj = v_form.save(commit=False)
            vacation_obj.user = request.user
            vacation_days = (
                vacation_obj.vacation_date_end - vacation_obj.vacation_date_start
            )
            vacation_obj.vacation_days = vacation_days.days
            vacation_obj.save()
            return redirect("users:vacation")
    else:
        v_form = VacationUpdateForm()

    context = {
        "v_form": v_form,
        "users_vacations": users_vacations
    }
    return render(request, template, context)


class VacationDeleteView(DeleteView):
    model = Vacation
    success_url = reverse_lazy("users:index")
