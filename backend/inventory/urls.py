from django.urls import path, include
from inventory import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.inventory_list),    
    path('all/', views.inventory_list),    
    path('<str:productID>/',views.get_product_by_id),
    path('<pk>/', views.inventory_list),    
    path('create/', views.createProduct),
    path('upload/', views.uploadImage),
    path('update/<str:pk>', views.updateProduct),
    path('delete/<str:pk>', views.deleteProduct),
    
]
