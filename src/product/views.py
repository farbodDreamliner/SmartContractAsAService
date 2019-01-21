from django.shortcuts import render

from .models import Product, User

from .forms import UserForm, RawUserForm

# Create your views here.
# def product_detail_view(request):
        # obj = Product.objects.get(id=2)
        # context = {
        #         "title" : obj.title,
        #         "description" : obj.description
                
        # }
        # context = {
        #         'object': obj
        # }
        # return render(request, "product/detail.html", context)

# def user_creat_view(request):
#         form = UserForm(request.POST or None)
#         if form.is_valid():
#                 form.save()
#                 form = UserForm()

#         context = {
#                 'form': form
#         }
#         return render(request, "user/user_signup.html", context)

def user_creat_view(request):
        my_form = RawUserForm()
        if request.method == "POST":
                my_form = RawUserForm(request.POST)
                if my_form.is_valid():
                        print(my_form.cleaned_data)
                        User.objects.create(**my_form.cleaned_data)
                else:
                        print(my_form.errors)

        context = {
                'form' : my_form
        }
        return render(request, "user/user_signup.html", context)