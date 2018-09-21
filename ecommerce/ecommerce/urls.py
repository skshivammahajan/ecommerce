"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .views import home_page, home, about, contact, login_user, register_user
from django.views.generic import TemplateView
from products.views import ProductListView, product_list_view, product_detail_view, ProductDetailView

urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'', home, name="home"),
    path(r'about/', about, name="about"),
    path(r'contact/', contact, name="contact"),
    path(r'login/', login_user, name="login"),
    path(r'register/', register_user, name="register"),
    path('bootstrap/', TemplateView.as_view(template_name="bootstrap/example.html")),
    path('product/', include('products.urls')),
# path(r'products/', ProductListView.as_view()),
# path(r'products-fbv/', product_list_view),
# path(r'product-detail/(?P<pk>\d+)/$', ProductListView.as_view()),
# path(r'products-detail-fbv/?P<pk>\d+/$', product_list_view)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)