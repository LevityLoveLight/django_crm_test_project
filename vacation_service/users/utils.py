from django.core.paginator import Paginator

from vacation_service import settings


def vacation_per_page(request, vacation_list):
    paginator = Paginator(vacation_list, settings.VACATIONS_0N_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj
