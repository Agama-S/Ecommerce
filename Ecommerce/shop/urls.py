from .import views
from django.urls import path

urlpatterns = [
    path('', views.allproducts, name='allproducts'),


    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('account/', views.account, name='account'),
    path('signout/', views.signout, name='signout'),
    path('delete/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_catdetail'),


]
