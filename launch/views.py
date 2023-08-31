from django.shortcuts import render

def launch(request):
    return render(request, 'launch/index.html')
