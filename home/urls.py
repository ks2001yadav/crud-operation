from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('details/',views.details,name="details"),
    path('details/update/<int:id>/', views.update,name='update'),
    path('details/edit/<int:id>/', views.edit,name='edit'),
    path('details/delete/<int:id>/', views.delete,name='delete'),
]
