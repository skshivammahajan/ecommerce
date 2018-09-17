from django.urls import path, include, re_path
from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products-fbv/', views.product_list_view),
    re_path(r'^product-detail/(?P<pk>\d+)/$', views.ProductDetailView.as_view()),
    re_path(r'^products-detail-fbv/(?P<pk>\d+)/$', views.product_detail_view)
]