from django.shortcuts import render

def qna(request):
    return render(request, 'qna/qna.html')

def qna_details(request, pk):
    return render(request, 'qna/qna_details.html')