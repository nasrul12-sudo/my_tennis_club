from django.urls import path
from . import views

urlpatterns = [
    path('', views.member, name='index'),
    # path('user/', views.user, name='user'),
    path('buku', views.buku, name='buku'),
    path('billing/', views.billing, name='billing'),
    path('jurnal', views.jurnal, name='jurnal'),
    path('transaksi/', views.transaksi, name='transaksi'),
    path('upload/', views.upload_excel, name='upload_excel'),
    # path('upload_success/', views.upload_success, name='upload_success'),
]