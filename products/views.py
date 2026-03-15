from django.views.generic import ListView, DetailView

from products.models import Product, ProductCategory, ProductTag, ProductColor, Manufacture, ProductStatus


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        products = Product.objects.filter(is_active=True).order_by('-id')

        categories = self.request.GET.getlist('cat')
        tags = self.request.GET.getlist('tag')
        manufacture = self.request.GET.get('manufacture')

        categories_id_list = []
        tags_id_list = []

        if categories:
            categories_id_list = list(map(int, categories[0].split(',')))
        if tags:
            tags_id_list = list(map(int, tags[0].split(',')))

        if categories_id_list:
            products = products.filter(categories__id__in=categories_id_list)
        if tags_id_list:
            products = products.filter(tags__id__in=tags_id_list)
        if manufacture:
            products = products.filter(manufacture__id=int(manufacture))

        return products.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.filter(is_active=True)
        context["tags"] = ProductTag.objects.all()
        context["colors"] = ProductColor.objects.all()
        context["manufactures"] = Manufacture.objects.filter(is_active=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'

    def get_object(self):
        obj = super().get_object()
        if not obj.is_active:
            from django.http import Http404
            raise Http404
        return obj