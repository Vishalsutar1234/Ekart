from django.urls import path
from ecomapp import views
urlpatterns = [
    path('',views.home),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('addition/<x>/<y>',views.addition),
    path('productlist',views.product_list),
    path('base',views.reuse),
    path('sort/<sv>',views.sort),
    path('catfilter/<catv>',views.catfilter),
    path('pricefilter/<pv>',views.pricefilter),
    path('pricerange',views.pricerange),
    path('pdetails/<pid>',views.product_details),
    path('addproduct',views.addproduct),
    path('delproduct/<rid>',views.delproduct),
    path('editproduct/<rid>',views.editproduct),
    path('djangoform',views.djangoform),
    path('modelform',views.modelform),
    path('register',views.user_register),
]