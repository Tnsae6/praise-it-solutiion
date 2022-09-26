from django.shortcuts import render
#from django.core.mail import send_mail
from django.http import Http404


from post.models import *
from about.models import experts

# Create your views here.
# crud create retrive update delete
address = Address.objects.all()
links_objects = links.objects.all()
icons_obj = icons.objects.all()

OurServices_obj = OurServices.objects.all()
AdditionalServices_obj = AdditionalServices.objects.all()

def index(request):
    post_objects = post.objects.all()
    homeslider_obj = homeslider.objects.all
    address = Address.objects.all()
    links_objects = links.objects.all()
    icons_obj = icons.objects.all()
    OurServices_obj = OurServices.objects.all()
    AdditionalServices_obj = AdditionalServices.objects.all()
    expert_obj = experts.objects.all()
    context = {
        'slider': homeslider_obj,
        'posts': post_objects,
        'link': links_objects,
        'address': address,
        'expert' : expert_obj,       
        'icons': icons_obj,
        'additionalservices': AdditionalServices_obj,
    }
    return render(request, "posts/index.html", context)


#def contact(request):
#     MapAddress_obj = MapAddress.objects.all()
#     context = {
#         'address': address,
#         'icons': icons_obj,
#         'map': MapAddress_obj,
#     }

#     if request.method == "POST":
#         message_name = request.POST["Name"]
#         message_email = request.POST["Email"]
#         message_phone = request.POST["Phone"]
#         message_subject = request.POST["Subject"]
#         message = request.POST["Message"]

#         contact_Info = ContactUSInfo(message_name=message_name, message_email=message_email,
#                                      message_phone=message_phone, message_subject=message_subject, message=message)
#         contact_Info.save()
#         return render(request, "posts/contact.html", context)

#     else:

#        return render(request, "posts/contact.html")


def service(request):
    context = {
#        'posts': post_objects,
        'link': links_objects,
        'address': address,
        'icons': icons_obj,

    }

    return render(request, "posts/service.html", context)


# def about(request):
#     context = {
#         'posts': post_objects,
#         'link': links_objects,
#         'address': address,
#         'icons': icons_obj,
#     }

#     return render(request, "posts/about.html", context)


def shop(request):
    post_objects = post.objects.all()
    context = {
        'posts': post_objects,
        'link': links_objects,
        'address': address,
        'icons': icons_obj,
    }
    return render(request, "posts/shop.html", context)


def handler404(request, exception):
    context = {
 #       'posts': post_objects,
        'link': links_objects,
        'address': address,
        'icons': icons_obj,
    }

    return render(request, "posts/404.html", context)


def team(request):
    post_objects = post.objects.all()
    context = {
        'posts': post_objects,
        'link': links_objects,
        'address': address,
        'icons': icons_obj,
    }

    return render(request, "posts/team.html", context)


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
