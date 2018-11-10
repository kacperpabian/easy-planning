from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Start page</h1>")


def detail(request, schedule_id):
    return HttpResponse("<h2>Details for Schedule id: " + str(schedule_id) + "</h2>")
