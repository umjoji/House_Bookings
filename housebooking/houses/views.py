from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HouseRegistration, ImageUpload, AddAmenity
from .models import HouseImages, House, Amenity
from django.conf import settings
from landlords.models import AgentAssignment
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import HouseFilter
from landlords.models import LandLord

# Create your views here.
def house_reg(request):
    if request.method == "POST":
        form = HouseRegistration(request.POST)
        if form.is_valid():
            house = form.save(commit=False) #saves the form but not commit to the database yet
            return redirect('preview_house', house_id=house.house_id)
    else:
        form = HouseRegistration()
    context = {'form': form}
    return render(request, "register_house.html", context)

class HouseListView(FilterView):
    model = House
    paginate_by = 10
    filterset_class = HouseFilter
    template_name = 'houses/house_search.html'


class HouseCreateView(CreateView):
    model = House
    fields = ['name',
              'address',
              'city_id',
              'state_id',
              'amenities',
              'number_of_beds',
              'number_of_bath',
              'pet_allowed',
              'smoking_allowed',
              'description',
              'status',
    ]


    def form_valid(self, form):
        form.instance.landlord = LandLord.objects.get(landlord=self.request.user) # type: ignore
        form.save()
        return redirect('image-upload')

class HouseUpdateView(UpdateView):
    model = House
    fields = '__all__'

class HouseDeleteView(DeleteView):
    model = House
    success_url = reverse_lazy('houses')

class HouseDetailView(DetailView):
    model = House


class UploadView(FormView):
    template_name = 'upload_image.html'
    form_class = ImageUpload
    success_url = 'all'

    def form_valid(self, form) -> HttpResponse:
        for each in form.cleaned_data['media']:
            HouseImages.objects.create(file=each) # type: ignore
        return super(UploadView, self).form_valid(form)

def preview_house(request, house):
    house = House.objects.get(house=house)
    landlord = LandLord.landlord
    images = HouseImages.objects.filter(house=house) # type: ignore
    return render(request, 'houses/preview_house.html', {'house': house, 'images': images, 'landlord': landlord})


def image_list(request):
    images = HouseImages.objects.filter()
    return render(request, 'image_list.html', {'images': images})

def add_amenities(request):
    if request.method == 'POST':
        form = AddAmenity(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_amenities')

# class AmenitiesView(TemplateView):
#     template_name = 'search.html'

# class AmenitiesResultsView(ListView):
#     model = Amenity
#     template_name = 'search1.html'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Amenity.objects.filter(
#             Q(name__icontains=query) | Q(name__icontains=query)
#         )
#         return object_list

class HouseView(TemplateView):
    template_name = 'houses/house_search.html'

class HouseResultsView(ListView):
    model = House
    template_name = 'houses/house_search1.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = House.objects.filter(
            Q(name__icontains=query)
        )

        return object_list