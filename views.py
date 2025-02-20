from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render

def home(request):
    return render(request, 'home/TrangChu.html')  # Đảm bảo có template `home.html`
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')
def logout(request):
    return render(request, 'registration/logout.html')

def about_view(request):
    return render(request, 'home/about.html')

def trangchu(request):
    return render(request, 'home/TrangChu.html')

def trangcanhan(request):
    return render(request, 'home/TrangCaNhan.html')

def lophocchitiet(request):
    return render(request, 'home/LopHocChiTiet.html')

def lophoc(request):
    return render(request, 'home/LopHoc.html')

def dangbai(request):
    return render(request, 'home/DangBai.html')

def about(request):
    return render(request, 'home/about.html')