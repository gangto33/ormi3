from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def accounts_login(request):
    return render(request, 'accounts_login.html')

def accounts_logout(request):
    return render(request, 'accounts_logout.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')
