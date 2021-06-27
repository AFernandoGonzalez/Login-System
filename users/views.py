from django.shortcuts import render

def homeview(request):
    return render(request, 'users/home.html')
