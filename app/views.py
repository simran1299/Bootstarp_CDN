from django.shortcuts import render

# Create your views here.
def static_img(request):
    return render(request,'static_img.html')

def second_pg(request):
    return render(request,'second_pg.html')

def third_pg(request):
    return render(request,'third_pg.html')