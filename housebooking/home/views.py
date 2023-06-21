from django.shortcuts import render
from houses.models import House, HouseImages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.hashers import make_password
from .forms import UserCreateForm
from django.contrib import messages

# Create your views here.

def index(request):
    houses_available = House.objects.filter(status__exact='a')

    context = {
        'houses_available': houses_available,
    }

    return render(request, 'index.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            fm = form.save(commit=False)
            fm.save()
            messages.success(request, f'{username} Successfully registered')
            form = UserCreateForm()
        return render(request, 'index.html', {'form': form})
    else:
        form = UserCreateForm()
        context = {'form': form,}
    return render(request, 'auth/user_form.html', {'form': form})

class UserDetailView(DetailView):
    model = User
    template_name = 'landlords/landlord_detail.html'
    fields = ['first_name',
              'last_name',
              'email',
              'username',
              'password',
              'phone_number',
    ]

def preview_user(request, pk):
    pk = User.objects.get(pk=pk)
    return render(request, 'landlords/landlord_detail.html', {'pk': pk})
# class CreateUserView(CreateView):
#     model = User
#     fields = ['first_name',
#               'last_name',
#               'email',
#               'username',
#               'password'
#     ]

#     success_url = 'index/'



def about_us(request):
    return render(request, "about.html")