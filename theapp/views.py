from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def logged(request):
    return render(request, 'logged.html')

def register(request):
    return render(request, 'register.html')
    
def cafe(request):
    return render(request, 'cafe.html')

def food(request):
    return render(request, 'food.html')

def movie(request):
    return render(request, 'movie.html')

def mypage(request):
    return render(request, 'mypage.html')

def change(request):
    return render(request, 'change.html')

def about(request):
    return render(request, 'About.html')

def kiosk_1(request):
    return render(request, 'kiosk_1.html')

def kiosk_2(request):
    return render(request, 'kiosk_2.html')

def kiosk_3(request):
    return render(request, 'kiosk_3.html')

def kiosk_4(request):
    return render(request, 'kiosk_4.html')

def kiosk_5(request):
    return render(request, 'kiosk_5.html')

def kiosk_6(request):
    return render(request, 'kiosk_6.html')

def kiosk_7(request):
    return render(request, 'kiosk_7.html')
    
