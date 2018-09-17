from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render , get_object_or_404
from .models import Product


# Class-Based-View
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product_list.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     print("Calling Product List")
    #     context = super(ProductListView, self).get_context_data(*kwargs, **kwargs)
    #     print(context)
    #     return context
    #      object_list is the required context


# Function_Based-View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product_list.html", context)


# Class-Based-View
class ProductDetailView(DetailView):
    # model = Product
    # # queryset = get_object_or_404(Product)
    queryset = Product.objects.all()
    template_name = "product_detail.html"

    # def get_object(self):
    #     product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     print(product)
    #     return self.model.objects.filter(pk=self.kwargs['pk'])

    # def get_context_data(self, *args, **kwargs):
    #     print("Calling Product De")
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
         # object_list is the required context


# Function_Based-View
def product_detail_view(request, *args, **kwargs):
    # queryset = get_object_or_404(Product, pk=kwargs['pk'])
    # print(queryset)
    # try:
    #     instance = Product.objects.get(pk=kwargs['pk'])
    # except Product.DoesNotExist:
    #     raise Http404("Product Doesn't Exist.")
    # except Exception:
    #     print("Something Went Wrong.")

    qs = Product.objects.filter(pk=kwargs['pk'])
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product Doesn't Exist.")

    context = {
        "object": instance
    }
    return render(request, "product_detail.html", context)