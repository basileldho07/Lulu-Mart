from django.urls import path
from Frontend import views

urlpatterns = [
    path('Frontend_page/', views.Frontend_page,name="Frontend_page"),
    path('product_page/<catname>/', views.product_page,name="product_page"),
    path('single_product/<int:proid>/', views.single_product,name="single_product"),
    path('contact_page/', views.contact_page,name="contact_page"),
    path('Contact_save/', views.Contact_save,name="Contact_save"),
    path('Userlogin/', views.Userlogin,name="Userlogin"),
    path('User_save/', views.User_save,name="User_save"),
    path('Admin_login/', views.Admin_login,name="Admin_login"),
    path('Cart/', views.Cart,name="Cart"),
    path('car_save/', views.car_save,name="car_save"),
    path('Checkout/', views.Checkout,name="Checkout"),
    path('checkout_save/', views.checkout_save,name="checkout_save"),
]