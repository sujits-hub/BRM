from django.urls import path
from django.conf.urls import url,include
from brmapp import views
urlpatterns = [
    path('',views.userlogin),
    path('view-books',views.viewbooks),
    path('edit-book',views.editbook),
    path('delete-book',views.deletebook),
    path('search-book',views.searchbook),
    path('send',views.send),
    path('search',views.search),
    path('edit',views.edit),
    path('new-book',views.newbook),
    path('userlogout',views.userlogout),
    path('userlogin',views.userlogin),
    
]

