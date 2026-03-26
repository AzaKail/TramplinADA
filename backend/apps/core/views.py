from django.http import JsonResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/index.html"


def healthcheck(request):
    return JsonResponse({"status": "ok", "service": "tramplin-ada"})