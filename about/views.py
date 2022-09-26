from django.shortcuts import render
from about.models import *
from post.models import *
# Create your views here.


def about(request):
    values_obj = values.objects.all()
    mission_obj = mission.objects.all()
    vision_obj = vision.objects.all()
    welcome_obj = welcome.objects.all() 
    experts_obj = experts.objects.all()
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
        'value':values_obj,
        'missions':mission_obj,
        'visions': vision_obj,
        'welcomes': welcome_obj,
        'expert': experts_obj,
    }

    return render(request, "posts/about.html", context)


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
