from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def info_main(request):
    return render(request, 'info_main.html')


def info_art(request, painting_slug):
    if painting_slug == 'men-1':
        return render(request, 'men_1.html')
    if painting_slug == 'women-1':
        return render(request, 'women_1.html')
    if painting_slug == 'men-2':
        return render(request, 'men_2.html')

    else:
        return render(request, 'page_404.html', status=404)






