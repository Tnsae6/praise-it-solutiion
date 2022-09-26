from django.shortcuts import render

# Create your views here.
from service.models import *
from post.models import *
faq_obj = faq.objects.all()

def service(request):
    intro_obj = intro.objects.all()
    main_service_obj = main_service.objects.all() 
    add_service_obj = additionalservices.objects.all()
    Benefits_obj = Benefit.objects.all()
    Techlevel_obj = Technologylevel.objects.all()
    choose_service_obj = main_service.objects.order_by('-timestamp')[:3]
    address = Address.objects.all()
    links_objects = links.objects.all()
    icons_obj = icons.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    context = {
        'intros': intro_obj,
        'choose_service' : choose_service_obj,
        'main_service' : main_service_obj,
        'add_service' : add_service_obj,
        'benefits' : Benefits_obj,
        'techlevel' : Techlevel_obj,
        'faq' : faq_obj,
        'link': links_objects,
        'service': OurServices_obj,
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
        'address': address,

    }
    return render(request,"posts/service.html", context)

def main_service(request, id):
    return render(request)
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

def faq(request):
    # faq_obj = faq.objects.all()

    context = {
        'faq' : faq_obj,
    }
    return render(request, "posts/faq.html", context)

