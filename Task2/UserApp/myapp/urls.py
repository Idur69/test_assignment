from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, api_views

urlpatterns = [
    path('',views.home,name='home'),

    path('register/', views.register, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'),
         name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'),
         name="users-logout"),
    path('hgfjhjdgUserList/', api_views.user_listview_api),
    path('products/', views.products, name="products"),
]
