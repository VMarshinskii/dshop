# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, Http404, redirect
from django.template.context_processors import csrf
from django.utils.encoding import smart_str
from cart.models import CartProduct
from dshop.additions import upload_file
from catalog.models import Category, Product
from models import SiteSettings
from forms import SiteSettingsForm
import simplejson as json
from simplejson.compat import StringIO


def video_upload(request):
    if request.method == 'POST' and request.user.is_authenticated():
        f = request.FILES['file']
        path = "/static/uploads/"
        url = upload_file(f, path)
        return HttpResponse(url)
    return HttpResponse("no")


def sort_list():
    mass_object = []
    roots = Category.objects.filter(parent=None, public=True)

    def rec_list(obj):
        obj.title = smart_str("— "*obj.step) + smart_str(obj.title)
        mass_object.append(obj)
        children = Category.objects.filter(parent=obj, public=True)

        for child in children:
            rec_list(child)

    for root in roots:
        rec_list(root)

    return mass_object


def tree_categories(request, id=-1):
    if request.user.is_authenticated():
        return render_to_response("tree_categories.html", {
            'categories': sort_list(),
        })
    raise Http404


def admin_settings(request):
    if request.user.is_authenticated():
        args = {}
        args.update(csrf(request))
        try:
            model = SiteSettings.objects.get(id=1)
            args['form'] = SiteSettingsForm(instance=model)
        except SiteSettings.DoesNotExist:
            args['form'] = SiteSettingsForm()

        if request.POST:
            form = SiteSettingsForm(request.POST, request.FILES)
            if form.is_valid():
                model = form.save(commit=False)
                model.id = 1
                model.save()
                return redirect('/admin/')
            else:
                args['form'] = form

        return render_to_response("admin_settings.html", args)
    else:
        return redirect('/admin/')


def get_products_list(request):
    mass_id = []

    for id in request.GET.get("mass_id", "").split(","):
        if id != "":
            mass_id.append(int(id))

    sum_all = 0

    products = []
    for product in CartProduct.objects.filter(id__in=mass_id):
        product.sum = product.cart_price * product.cart_count
        sum_all += product.cart_price * product.cart_count
        products.append(product)

    return render_to_response("get_products_list.html", {'products': products, 'sum': sum_all})


def update_product_sort(request):
    if request.user.is_authenticated() and request.GET:
        sorts = request.GET['sorts']
        for pr_id, pr_sort in json.loads(sorts).items():
            try:
                product = Product.objects.get(id=int(pr_id))
                print str(product.id) + " == " + pr_sort
                product.sort = pr_sort
                if product.save():
                    print str(product.id) + " == " + product.sort
                else:
                    print "false"
            except Product.DoesNotExist:
                pass
        return HttpResponse('ok')

    raise Http404()


def update_category_sort(request):
    if request.user.is_superuser:
        try:
            category = Category.objects.get(id=int(request.GET.get('category_id')))
            sort_type = request.GET.get('sort_type')

            if sort_type == "up":
                category_prev = None
                for root in Category.objects.filter(parent=None).order_by('sort'):
                    if category.id == root.id:
                        if category_prev:
                            category_prev.sort, category.sort = category.sort, category_prev.sort
                            category_prev.save()
                            category.save()
                        return HttpResponse(json.dumps({'error': False}))
                    category_prev = root

            if sort_type == "down":
                category_prev = None
                for root in reversed(Category.objects.filter(parent=None).order_by('sort')):
                    if category.id == root.id:
                        if category_prev:
                            category_prev.sort, category.sort = category.sort, category_prev.sort
                            category_prev.save()
                            category.save()
                        return HttpResponse(json.dumps({'error': False}))
                    category_prev = root

        except Category.DoesNotExist:
            return HttpResponse(json.dumps({'error': True}))
    raise Http404()