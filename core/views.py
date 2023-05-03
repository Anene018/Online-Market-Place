from django.shortcuts import render ,redirect
from item.models import Category,Item
from . import forms
# Create your views here.
# Index view
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render( request,'core/index.html',
    {
        'categories':categories,
        'items':items,
    },
    )

# Contact view
def contact(request):
    return render( request, 'core/contact.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:

        form = forms.SignupForm()

    return render (request , 'core/signup.html',{
        'form':form,
    })

def login(request):
    return render(request ,'core/login.html')