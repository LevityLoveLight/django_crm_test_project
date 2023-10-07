from django.shortcuts import render

from .models import User


def index(request):
    template = 'users/index.html'
    post_list = User.objects.select_related(
    ).all()
    context = {
        # 'page_obj': posts_per_page(request, post_list),
    }
    return render(request, template, context)
