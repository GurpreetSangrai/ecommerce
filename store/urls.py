from django.contrib import admin
from django.urls import path 
from django.conf.urls import include, url
from .views.home import Index
from .views.signup import Signup 
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView


urlpatterns = [
   url(r'^$',Index.as_view(), name= 'homepage'),
   url(r'^signup/$', Signup.as_view(), name = 'signup'),
   url(r'^login/$', Login.as_view(), name = 'login'),
   url(r'^logout/$', logout , name = 'logout'),
   url(r'^cart/$', Cart.as_view() , name = 'cart'),
   url(r'^check-out$', CheckOut.as_view() , name = 'checkout'),
   url(r'^orders$', OrderView.as_view(), name='orders'),

]

   