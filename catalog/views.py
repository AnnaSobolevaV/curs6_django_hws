import datetime

from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionProductForm
from catalog.models import Category, Product, BlogRecord, Contacts, Version
from unidecode import unidecode


class ContactsCreateView(CreateView):
    model = Contacts
    template_name = 'catalog/contacts.html'
    fields = ("name", "phone", "message")
    success_url = reverse_lazy('catalog:contacts')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context


def without_category(request):
    product_list_wo_category = Product.objects.filter(category=None)
    category_list = Category.objects.all()
    context = {'product_list_wo_category': product_list_wo_category,
               'category_list': category_list}
    return render(request, 'catalog/category_detail.html', context)


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        product_list = Product.objects.filter(category=self.object.id)
        context['product_list'] = product_list
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data['object_list']:
            is_current_vers = Version.objects.filter(product=product, is_current_vers=True).first()
            product.is_current_vers = is_current_vers
        category_list = Category.objects.all()
        context_data['category_list'] = category_list
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product = context_data['object']
        is_current_vers = Version.objects.filter(product=product, is_current_vers=True).first()
        product.is_current_vers = is_current_vers
        category_list = Category.objects.all()
        context_data['category_list'] = category_list
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionProductForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
            context['formset'] = formset
        else:
            formset = version_formset(instance=self.object)
            context['formset'] = formset
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionProductForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
            context['formset'] = formset
        else:
            formset = version_formset(instance=self.object)
            context['formset'] = formset
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()

        formset = context_data['formset']
        print(formset)
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count += 1
        self.object.save()
        return self.object


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = ("header", "is_published", "content", "preview")
    success_url = reverse_lazy('catalog:blogrecord_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(unidecode(new_rec.header + ' ' + str(new_rec.pk)))
            new_rec.created_at = datetime.date.today()
            new_rec.save()

        return super().form_valid(form)


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ("header", "is_published", "content", "preview")
    success_url = reverse_lazy('catalog:blogrecord_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(unidecode(new_rec.header + ' ' + str(new_rec.pk)))
            new_rec.updated_at = datetime.datetime.now()
            new_rec.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blogrecord', args=[self.kwargs.get('pk')])


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('catalog:blogrecord_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_list = Category.objects.all()
        context['category_list'] = category_list
        return context
