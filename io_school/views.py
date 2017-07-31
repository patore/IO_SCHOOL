from django.shortcuts import render


def Home(request):

    return render(request, 'defaults/home.html')