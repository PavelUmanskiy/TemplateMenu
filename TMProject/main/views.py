from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html', context={'a': 1})


def example_view(request):
    return render(request, 'default.html')
