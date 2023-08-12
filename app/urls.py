from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Importants
    path('', home,name='home'),
    path('description/<str:id>',EventDescription,name='EventDescription'),
    # path('cart/',cart,name='cart'),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('search/',search,name="search"),
    path('wishlist/',wishlist,name="wishlist"),

    # auth
    path('register/',User_Register,name='User_Register'),
    path('login/',User_Login,name='User_Login'),
    path('logout/',User_Logout,name='User_Logout'),

    # CART
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart_detail/',cart_detail,name='cart_detail'),

     #Checkout
     path('checkout/',checkout,name="checkout") 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)