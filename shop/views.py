from django.shortcuts import render

# Create your views here.
from shop.models import Items, set, single
from post.models import *

def shop(request):
    set_obj = set.objects.all()
    Item_obj = Items.objects.all()
    single_obj = single.objects.all()

    address = Address.objects.all()
    links_objects = links.objects.all()
    icons_obj = icons.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    context = {
        'sets':set_obj,
        'single' : single_obj,
        'item' : Item_obj,
        'link': links_objects,
        'service': OurServices_obj,
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
        'address': address,
    }

    return render(request, "posts/shop.html", context)
def base(request):
    
    address = Address.objects.all()
    links_objects = links.objects.all()
    icons_obj = icons.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    context = {

        'link': links_objects,
        'service': OurServices_obj,
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
        'address': address,
    }
    return render(request, "posts/base.html", context)


def base(request):

    address = Address.objects.all()
    links_objects = links.objects.all()
    icons_obj = icons.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    context = {

        'link': links_objects,
        'service': OurServices_obj,
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
        'address': address,
    }
    return render(request, "posts/base.html", context)
