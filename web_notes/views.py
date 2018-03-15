from django.shortcuts import render

# Create your views here.


def notesheet(request):
    return render(request, 'web-notes/note.html')
