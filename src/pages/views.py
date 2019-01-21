from django.http import HttpResponse
from django.shortcuts import render

# from .forms import userForm


# Create your views here.
def home_view(request, *args, **kwargs):
        #return HttpResponse("<h1>Hello World</h1>")
        return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
        #return HttpResponse("<h1>Contact Page</h1>")
        return render(request, "contact.html", {})
        

def about_view(request, *args, **kwargs):
        #return HttpResponse("<h1>About Page</h1>")
        my_context = {
                "my_text": "This is about us",
                "my_number": 989221245425,
                "my_list": ["behnamifarbod@gmail.com", "behnamifarbod@blockchainlabs.ir", "GTMD.iut.ac.ir", 321, "Abc"]
        }
        return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
        return HttpResponse("<h1>Social Page</h1>")


# def user_creat_view(request, *args, **kwargs):
#         form = userForm(request.POST or None)
#         if form.is_valid():
#                 form.save()

#         context = {
#                 'form': form
#         }
#         return render(request, "user/user_signup.html", context)