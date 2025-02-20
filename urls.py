from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.trangchu, name='trangchu'),
    path('trang-ca-nhan/', views.trangcanhan, name='trangcanhan'),
    path('lop-hoc-chi-tiet/', views.lophocchitiet, name='lophocchitiet'),
    path('lop-hoc/', views.lophoc, name='lophoc'),
    path('dang-bai/', views.dangbai, name='dangbai'),
    path('about/', views.about, name='about'),
]