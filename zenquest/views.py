from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


# categories views


def technology(request):
    return render(request, 'technology/3.html', {})


def nature(request):
    return render(request, 'nature/1.html', {})


def photography(request):
    return render(request, 'photography/1.html', {})


def travel(request):
    return render(request, 'travel/1.html', {})


def lifestyle(request):
    return render(request, 'lifestyle/1.html', {})


def sports(request):
    return render(request, 'sports/1.html', {})


def entertainment(request):
    return render(request, 'entertainment/1.html', {})