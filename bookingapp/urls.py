from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.userindex,name='userindex'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('branch',views.branch,name='branch'),
    path('register',views.register,name='register'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('contactdata',views.contactdata,name='contactdata'),
    path('logindata',views.logindata,name='logindata'),
    path('publicdata',views.publicdata,name='publicdata'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('salons/<str:category>',views.salons,name='salons'),
    path('services/<str:cat>',views.services,name='services'),
    path('single/<int:id>',views.single,name='single'),
    path('book/<int:id>',views.book,name='book'),
    path('bookdata/<int:id>',views.bookdata,name='bookdata'),
    path('history',views.history,name='history')
]
