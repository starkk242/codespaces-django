from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )


def new(request):
    return JsonResponse({"just": True})
