from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('',views.index ,name='index'),
path('collections',views.collection,name='collection'),
path('collectionview/<str:name>',views.collectionview,name='collection'),
path('collections/<str:cname>/<str:pname>',views.productdetail,name="productdetails"),
path('register',views.register,name="register"),
path('login',views.login_page,name="login"),
path('logout',views.logout_page,name="logout"),
path('cart',views.cart_page,name="cart"),
path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
path('addtocart',views.add_to_cart,name="addtocart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
# path('collections/<str>',views.collectionview,name='collections'),
# path('collectionsview',views.collectionview,name='collectionview'),
]
    
