from django.shortcuts import render


def aboutus_view(request):
    return render(request, 'otherpages/aboutus.html')


def contactus_view(request):
    return render(request, 'otherpages/contactus.html')


def index_views(request):
    return render(request, 'products/index.html')
