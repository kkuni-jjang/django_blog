from django.shortcuts import render

def portfolio_home(request):
    return render(request, 'portfolio/home.html')

def project1(request):
    return render(request, 'portfolio/project1.html')

def project2(request):
    return render(request, 'portfolio/project2.html')

def project3(request):
    return render(request, 'portfolio/project3.html')

