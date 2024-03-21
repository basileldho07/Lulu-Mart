 from django.urls import path
from Backend import views

urlpatterns = [
    path('lulu_page/', views.lulu_page,name="lulu_page"),
    path('Category/', views.Category,name="Category"),
    path('Category_save/', views.Category_save,name="Category_save"),
    path('Display_category/', views.Display_category,name="Display_category"),
    path('Edit_category/<int:p_id>/', views.Edit_category,name="Edit_category"),
    path('uptade_category/<int:p_id>/', views.uptade_category,name="uptade_category"),
    path('Product/', views.Product,name="Product"),
    path('Product_save/', views.Product_save,name="Product_save"),
    path('Display_products/', views.Display_products,name="Display_products"),
    path('Edit_products/<int:c_id>/', views.Edit_products, name="Edit_products"),
    path('uptade_products/<int:c_id>/', views.uptade_products, name="uptade_products"),
    path('Admin_login_page/', views.Admin_login_page,name="Admin_login_page"),
    path('Adminlogin/', views.Adminlogin,name="Adminlogin"),
    path('Adminlogout/', views.Adminlogout,name="Adminlogout"),
    path('Dispaly_contact/', views.Dispaly_contact,name="Dispaly_contact"),

]