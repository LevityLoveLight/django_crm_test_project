from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import User


@login_required()
def index(request):
    template = 'users/index.html'
    users_list = User.objects.all()
    print(users_list)
    context = {
        'users_obj': users_list,
    }
    return render(request, template, context)
