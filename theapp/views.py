from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'Login_page.html')
    

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