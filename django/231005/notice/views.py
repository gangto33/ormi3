from django.shortcuts import render

def notice(request):
    return render(request, 'notice/notice.html')

def free(request):
    return render(request, 'notice/free.html')

def post(request, pk):
    return render(request, 'notice/post.html')

def onenone(request):
    return render(request, 'notice/onenone.html')

def onenone1(request, pk):
    return render(request, 'notice/onenone1.html')