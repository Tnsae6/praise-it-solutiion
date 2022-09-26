from django.shortcuts import render
from contact.models import *
from post.models import *
# Create your views here.


def contact(request):
    MapAddress_obj = MapAddress.objects.all()
    icons_obj = icons.objects.all()
    address = Address.objects.all()
    links_objects = links.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    context = {
        'link': links_objects,
        'service': OurServices_obj,
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
        'address': address,
        'map': MapAddress_obj,
    }

    if request.method == "POST":
        message_name = request.POST["Name"]
        message_email = request.POST["Email"]
        message_phone = request.POST["Phone"]
        message_subject = request.POST["Subject"]
        message = request.POST["Message"]

        contact_Info = ContactUSInfo(message_name=message_name, message_email=message_email,
                                     message_phone=message_phone, message_subject=message_subject, message=message)
        contact_Info.save()
        return render(request, "posts/contact.html", context)

    else:

        return render(request, "posts/contact.html", context)


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
